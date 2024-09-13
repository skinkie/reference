import subprocess
import sys
import time
import json
import shlex
import os
import shutil


def clean_tmp(f):
    # Iterate over the items in the folder
    for item in os.listdir(f):
        item_path = os.path.join(f, item)

        if os.path.isfile(item_path):
            # Remove file if it matches the extensions
            if item.endswith('.duckdb') or item.endswith('.tmp'):
                try:
                    os.remove(item_path)
                except Exception as e:
                    print(f"Error while removing file: {e}")
        elif os.path.isdir(item_path):
            # Recursively clean subdirectory
            clean_tmp(item_path)

def clean(directory):
    # Clean the specified folder by deleting all files and subfolders
    # Iterate over the items in the directory
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isfile(item_path):
            # Remove file
            try:
                os.remove(item_path)
            except:
                print (f'Could not remove {item_path}')
        elif os.path.isdir(item_path):
            # Remove subdirectory and its contents
            try:
                shutil.rmtree(item_path)
            except:
                print (f'Could not remove {item_path}')



def main(script_file,log_file, todo_block,begin_step):
    # Read the scripts from a file
    with open(script_file) as f:
        data = json.load(f)

    with open(log_file, 'w') as f:
        for block in data:
            blockstop=False
            if  not todo_block==block["block"]:
                if not todo_block=="all":
                    continue
            scripts = block['scripts']
            step=1
            for script in scripts:
                if step<begin_step:
                    #skipping steps in the block
                    step=step+1
                    continue
                if blockstop==True:
                    break
                start_time = time.time()

                script_name = script['script']
                script_args = shlex.split(''.join(script['args']))

                # Write the script name to the log file with a starting delimiter
                f.write(f"--- {script_name} ---\n")
                if script_name.startswith("#"):
                    # is a comment
                    continue

                if script_name == 'clean_tmp':
                    # Execute the clean_tmp command
                    folder = script_args[0]
                    clean_tmp(folder)
                    f.write(f"Command 'clean_tmp' executed for folder: {folder}\n")
                    print(f"Command 'clean_tmp' executed for folder: {folder}\n")
                    continue

                if script_name == 'clean':
                    # Execute the clean command
                    folder = script_args[0]
                    clean(folder)
                    f.write(f"Command 'clean' executed for folder: {folder}\n")
                    print(f"Command 'clean' executed for folder: {folder}\n")
                    continue
                print(f"\n\n**************\nStarting script: {script_name} with {script_args}")
                # Fetch the Python executable
                python_executable = sys.executable
                # Run the script with arguments and capture the output
                command = python_executable + " " + script_name + " " + " ".join(
                    shlex.quote(arg) for arg in script_args)
                print(command)
                result = subprocess.run(command,
                                        stdout=subprocess.PIPE,
                                        stderr=subprocess.STDOUT,
                                        universal_newlines=True)
                end_time = time.time()
                execution_time = int(end_time - start_time)
                # Capture the output
                output = result.stdout

                # Print the output to the console
                print(output)

                # Write the output to the log file
                f.write(output)
                # Write the execution time to the log file
                f.write(f"Execution time: {execution_time} seconds\n")
                print(f"Execution time: {execution_time} seconds\n")

                if result.returncode == 0:
                    print(f'Script {script_name} terminated.')
                elif result.returncode == 1:
                    print(f'Script {script_name} returned an error. Terminating the block of scripts: {block['block']}')
                    f.write(f'Script {script_name} returned an error. Terminating the block of scripts: {block['block']}')
                    blockstop=True
                    break
                else:
                    print(f'Script {script_name} returned an unexpected error code: {result.returncode}.')
                    f.write(f'Script {script_name} returned an unexpected error code: {result.returncode}.')
                    blockstop=True
                    break


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Executes scripts')
    parser.add_argument('script_file', type=str, help='the script file')
    parser.add_argument('log_file', type=str, help='name of the log file')
    parser.add_argument('blockname', type=str, help='Block name to do')
    parser.add_argument('--begin_step', type=int, default=1, help='The begin step (default: 1)')
    args = parser.parse_args()

    main(args.script_file,args.log_file, args.blockname,args.begin_step)