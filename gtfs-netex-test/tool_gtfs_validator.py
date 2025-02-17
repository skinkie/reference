import logging
import os
import subprocess
import json
from aux_logging import *
import traceback

def print_stats(stats):
    log_all(logging.INFO,"GTFS Statistics:")
    for key, value in stats.items():
        log_all(logging.INFO,f"{key}: {value}")

def main(gtfs_file,res_folder):
    # Build the shell command
    command = f'java -jar ./gtfs-validator/gtfs-validator-6.0.0-cli.jar -i {gtfs_file} -o {res_folder}'
    log_all(logging.INFO,command)
    # Execute the command in the shell
    subprocess.run(command, shell=True)

    # Check the result files for errors
    report_file = os.path.join(res_folder, 'report.json')
    system_errors_file = os.path.join(res_folder, 'system_errors.json')

    # Check system_errors.json for notices
    with open(system_errors_file) as se_file:
        system_errors = json.load(se_file)
        if len(system_errors['notices']) == 0:
            log_all(logging.INFO,'No notices found in system_errors.json')
        else:
            log_all(logging.ERROR,'Notices found in system_errors.json')

    # Check report.json for notices with severity "ERROR"
    with open(report_file) as report_file:
        report_data = json.load(report_file)
        if 'notices' in report_data:
            for notice in report_data['notices']:
                if notice['severity'] == 'ERROR':
                    log_all(logging.ERROR, f"ERROR notice in report.json: {notice.get('code')}")

        else:
            log_all(logging.INFO, 'No notices found in report.json')

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Validates a gtfs file and shows some stats')
    parser.add_argument('gtfs_file', type=str, help='The input file (gtfs.zip)')
    parser.add_argument('res_folder', type=str, help='The folder for the report.')
    parser.add_argument('--log_file', type=str, required=False, help='the logfile')
    args = parser.parse_args()
    mylogger =prepare_logger(logging.INFO,args.log_file)

    try:
        main(args.gtfs_file, args.res_folder)
    except Exception as e:
        log_all(logging.ERROR, f'{e} {traceback.format_exc()}')
        raise e
