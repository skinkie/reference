import logging
import subprocess
import sys
import time
import json
import shlex
import os
import shutil
from aux_logging import *
from configuration import *

def replace_in_string(input, search, replace):
    return input.replace(search, replace)

# command to clean a directory from temp files (mostly duckdb)
def clean_tmp(f):
    # Iterate over the items in the folder
    if not os.path.isdir(f):
        log_all(logging.WARNING,"clean_tmp",f"No valid path to clean:{f}")

        return
    for item in os.listdir(f):
        item_path = os.path.join(f, item)

        if os.path.isfile(item_path):
            # Remove file if it matches the extensions
            if item.endswith('.duckdb') or item.endswith('.tmp'):  # logs are NOT cleaned (as at least one is already locked)
                try:
                    os.remove(item_path)
                except Exception as e:
                    log_print(f"Error while removing file: {e}")
        elif os.path.isdir(item_path):
            # Recursively clean subdirectory
            clean_tmp(item_path)

# removes a given processed folder
def clean(directory):
    # Clean the specified folder by deleting all files and subfolders
    if not os.path.isdir(directory):
        log_all(logging.WARNING,"clean_tmp",f"No valid path to clean: {directory}")
        return
    # Iterate over the items in the directory
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isfile(item_path):
            # Remove file
            try:
                os.remove(item_path)
            except:
                log_print (f'Could not remove {item_path}')
        elif os.path.isdir(item_path):
            # Remove subdirectory and its contents
            try:
                shutil.rmtree(item_path)
            except:
                log_print (f'Could not remove {item_path}')



def main(script_file,log_file, log_level, todo_block,begin_step):
    # blockexisted
    blockexisted=False
    # Read the scripts from a file
    with open(script_file) as f:
        data = json.load(f)

    # go through each block
    for block in data:
        processdir = processing_data + "/" + block["block"]

        blockstop = False
        if not todo_block == block["block"]:
            if not todo_block == "all":
                continue
        blockexisted=True
        scripts = block['scripts']
        prepare_logger(log_level, block["block"] + "/" + log_file)
        # log_once(logging.INFO, "Start", f'Processing block: {block["block"]}')
        step = 1
        for script in scripts:

            # skip some steps if this is mandated
            if step < begin_step:
                # skipping steps in the block
                step = step + 1
                continue
            if blockstop == True:
                break
            start_time = time.time()

            script_name = script['script']
            script_args = script['args']

            # replace the placeholder for processdir with the correct values and also the other place holders
            script_args = replace_in_string(script_args, "%%dir%%", processdir)
            script_args = replace_in_string(script_args, "%%block%%", block["block"])
            script_args = replace_in_string(script_args, "%%log%%", block["block"] + "/" + log_file)

            # if the processing dir doesn't exist, then we create it
            os.makedirs(processdir, exist_ok=True)

            # Write the script name to the log file with a starting delimiter
            log_all(logging.INFO, "test_runner", f"{script_name} with {script_args}")

            if script_name.startswith("#"):
                # is a comment and we do nothing
                continue

            if script_name == 'clean_tmp':
                # Execute the clean_tmp command
                folder = script_args
                clean_tmp(folder)
                log_all(logging.INFO, "test_runner", f"Command 'clean_tmp' executed for folder: {folder}\n")
                continue

            if script_name == 'clean':
                # Execute the clean command
                folder = script_args
                clean(folder)
                log_all(logging.INFO, "test_runner", f"Command 'clean' executed for folder: {folder}\n")
                continue
            # Fetch the Python executable
            python_executable = sys.executable

            # Run the script with arguments
            command = python_executable + " " + script_name + " " + script_args
            log_print(command)
            result = subprocess.run(command,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT,
                                    universal_newlines=True)
            end_time = time.time()
            execution_time = int(end_time - start_time)
            # Capture the output
            output = result.stdout

            # Print the output to the console
            log_print(output)

            # Write the execution time to the log file
            log_all(logging.INFO, "test_runner_timing", f"Execution time: {execution_time} seconds\n")
            log_write_counts(logging.WARNING)
            if result.returncode == 0:
                log_all(logging.DEBUG, "test_runner", f'Script {script_name} terminated.')
                log_flush()
            elif result.returncode == 1:
                log_all(logging.ERROR, "test_runner",
                        f'Script {script_name} returned an error. Terminating the block of scripts: {block['block']}')
                log_flush()
                blockstop = True
                break
            else:
                log_all(logging.ERROR, "test_runner",
                        f'Script {script_name} returned an unexpected error code: {result.returncode}.')
                log_flush()
                blockstop = True
                break
    if not blockexisted:
        log_all(logging.ERROR, "test_runner",
                f'Block "{todo_block}" not in script file.')
        log_flush()


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Executes scripts')
    parser.add_argument('script_file', type=str, help='the script file')
    parser.add_argument('log_file', type=str, help='name of the log file')
    parser.add_argument('blockname', type=str, help='Block name to do')
    parser.add_argument('--begin_step', type=int, default=1, help='The begin step (default: 1)')
    parser.add_argument('--log_level', type=int , default=logging.INFO, help='The begin step (default: 1)')
    args = parser.parse_args()

    main(args.script_file,args.log_file, args.log_level,args.blockname,args.begin_step)