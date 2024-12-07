import shlex
import subprocess
import sys
import time
import json
import shutil
from aux_logging import *
from configuration import *
import traceback


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


def parse_key_value_pairs(string):
    pairs = {}
    for pair in string.split(';'):
        key_value = pair.split('=')
        if len(key_value) == 2:
            key = key_value[0].strip()
            value = key_value[1].strip().strip('"').strip("'")  # Remove surrounding quotes from value
            pairs[key] = value
    return pairs
def set_defaults(keyvaluestr):
    result= parse_key_value_pairs(keyvaluestr)
    # replace what is not yet in defaults
    defaults.update(result)

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
        # make sure folder for block exists
        os.makedirs(processdir, exist_ok=True)
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

            if script_name == 'set_defaults':
                # Sets default values (when not done in configuration.py or local_configuration.py)
                set_defaults(script_args)
                log_all(logging.INFO, "test_runner", f"Command 'set_defaults' executed for: {script_args}\n")
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
            command_list = [python_executable,script_name]
            command_list.extend(shlex.split(script_args))
            result = subprocess.run(command_list,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT,
                                    universal_newlines=True)
            end_time = time.time()
            execution_time = int(10*(end_time - start_time))/10

            # Write the execution time to the log file
            log_all(logging.INFO, "test_runner_timing", f"Execution time: {execution_time} seconds\n")
            log_write_counts(logging.WARNING)
            log_flush()
            if result.returncode == 0:
                log_all(logging.DEBUG, "test_runner", f'Script {script_name} successfully terminated.')
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
    parser.add_argument('--log_level', type=int , default=logging.INFO, help='The log level (use logging constants)')
    args = parser.parse_args()
    mylogger = prepare_logger(logging.INFO, args.log_file)
    try:
        main(args.script_file, args.log_file, args.log_level, args.blockname, args.begin_step)
    except Exception as e:
        log_all(logging.ERROR, f'{e}', traceback.format_exc())
