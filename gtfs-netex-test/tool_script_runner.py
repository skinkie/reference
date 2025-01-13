import shlex
import subprocess
import sys
import time
import json
import shutil
from aux_logging import *
from configuration import *
import traceback
import urllib.request

def create_list_from_string(input_string):
    # Remove the square brackets from the string
    cleaned_string = input_string.strip('[]')
    # Split the cleaned string into a list using space as the delimiter
    result_list = cleaned_string.split(' ')
    return result_list

def check_string(input_string):
    if '[' in input_string and ']' in input_string:
        return True
    else:
        return False
def load_and_run(file_name, args_string):

    module_name = file_name[:-3]  # Remove the '.py' extension
    module_name = module_name+".main"
    components = module_name.split('.')
    mod = __import__(components[0])
    for comp in components[1:]:
        mod = getattr(mod, comp)
    args = args_string.split()  # Split the string into a list of arguments
    args1 = []
    for arg in args:
        if check_string(arg):
            arg= create_list_from_string(arg)
        elif arg == "True":
            arg=True
        elif arg == "False":
            arg=False
        args1.append(arg)
    result = mod(*args1)
    return result

def replace_in_string(input, search, replace):
    return input.replace(search, replace)

# command to clean a directory from temp files (mostly duckdb)
def clean_tmp(f):
    # Iterate over the items in the folder
    if not os.path.isdir(f):
        log_all(logging.WARNING,f"No valid path to clean:{f}")

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
        log_all(logging.WARNING,f"No valid path to clean: {directory}")
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


def download(folder, url):
    try:
        # Create the folder if it doesn't exist
        if not os.path.exists(folder):
            os.makedirs(folder)

        # Get the filename from the URL
        filename = os.path.basename(url)

        # Download the file
        urllib.request.urlretrieve(url, os.path.join(folder, filename))

        # Return the downloaded file path
        return os.path.join(folder, filename)

    except urllib.error.HTTPError:
        return "FILE NOT FOUND"

def remove_file(path):
    if os.path.isfile(path):
        try:
            os.remove(path)
            return "File removed successfully."
        except OSError as e:
            raise OSError(f"Failed to remove file: {str(e)}")
    else:
        raise FileNotFoundError(f"File not found: {path}")

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
        step = 0
        script_input_file_path = 'NOT SET YET'
        for script in scripts:
            step=step+1
            # skip some steps if this is mandated
            if step < begin_step:
                continue
            if blockstop == True:
                break
            start_time = time.time()

            script_name = script['script']
            script_args = script['args']
            script_download_url = block.get('download_url')
            # replace the placeholder for processdir with the correct values and also the other place holders
            script_args = replace_in_string(script_args, "%%dir%%", processdir)
            script_args = replace_in_string(script_args, "%%inputdir%%", input_dir)
            script_args = replace_in_string(script_args, "%%inputfilepath%%", script_input_file_path)
            script_args = replace_in_string(script_args, "%%block%%", block["block"])
            script_args = replace_in_string(script_args, "%%log%%", block["block"] + "/" + log_file)

            # if the processing dir doesn't exist, then we create it
            os.makedirs(processdir, exist_ok=True)

            # Write the script name to the log file with a starting delimiter
            log_all(logging.INFO, f"{block["block"]} - step: {step}: {script_name} {script_args}")

            if script_name.startswith("#"):
                # is a comment and we do nothing
                continue

            if script_name == 'set_defaults':
                # Sets default values (when not done in configuration.py or local_configuration.py)
                set_defaults(script_args)
                log_all(logging.INFO, f"Command 'set_defaults' executed for: {script_args}\n")
                continue

            if script_name == 'clean_tmp':
                # Execute the clean_tmp command
                folder = script_args
                clean_tmp(folder)
                log_all(logging.INFO,  f"Command 'clean_tmp' executed for folder: {folder}\n")
                continue

            if script_name == 'clean':
                # Execute the clean command
                folder = script_args
                clean(folder)
                log_all(logging.INFO,  f"Command 'clean' executed for folder: {folder}\n")
                continue
            if script_name == 'download_input_file':
                # Execute the download command. The file under the download_url is copied to a folder
                folder = script_args
                script_input_file_path=download(folder,script_download_url)
                log_all(logging.INFO, f"Command 'download_input_file' executed for url: {script_download_url}\n")
                continue
            if script_name == 'remove_file':
                # Execute the download command. The file under the download_url is copied to a folder
                remove_file(script_input_file_path)
                log_all(logging.INFO, f"Command 'remove_file' executed for file: {script_input_file_path}\n")
                continue
            result=load_and_run(script_name, script_args)
            end_time = time.time()
            execution_time = int(10*(end_time - start_time))/10

            # Write the execution time to the log file
            log_all(logging.INFO,  f"Execution time: {execution_time} seconds for {block["block"]} - step: {step}: {script_name} {script_args}\n")
            log_write_counts(logging.WARNING)
            log_flush()
            if result == None or result == 0:
                log_all(logging.DEBUG, f'Script {script_name} successfully terminated.')
                log_flush()
            elif result == 1:
                log_all(logging.ERROR, f"Script {script_name} returned an error. Terminating the block of scripts: {block['block']}")
                log_flush()
                blockstop = True
                break
            else:
                log_all(logging.ERROR, f'Script {script_name} returned an unexpected error code: {result.returncode}.')
                log_flush()
                blockstop = True
                break
    if not blockexisted:
        log_all(logging.ERROR, f'Block "{todo_block}" not in script file.')
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
        log_all(logging.ERROR, f'{e} {traceback.format_exc()}')
