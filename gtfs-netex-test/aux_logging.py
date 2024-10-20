#  We will have logging based on the standard logging
# https://docs.python.org/3/howto/logging.html
# --log=INFO
# --logfile=filename

from configuration import *
import os

# Basic ideas:
# - There might still remain print statements, that are just send to the screen
# - we still wrap them to make sure, we can deactivate it
# - log level can be set
# - There is a standard log (log format)
# - Some logs have special purposes (e.g. the script protocol, outputs with lists)
# - some things are corrected and only one problem is resolved.
# - the logging should assist the pipeline.

def log_print(s):
    global NOSOFTLOGGING
    if not NOSOFTLOGGING:
        print(s)

def prepare_logger(log_level,log_file_name):
    # create logger
    global mylogger
    global log_dict
    global processing_data
    if not mylogger:
        mylogger = logging.getLogger("testrunner")
        if mylogger:
            mylogger.setLevel(log_level)
            log_dict = {}
            # create console handler and set level to debug
            ch = logging.StreamHandler()
            ch.setLevel(logging.DEBUG)

            # create formatter
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

            # add formatter to ch
            ch.setFormatter(formatter)
            mylogger.addHandler(ch)

            # add ch to logger
            if not log_file_name == None and len(log_file_name) > 5:
                # if the processing dir doesn't exist, then we create it
                directory = os.path.dirname(processing_data + "/" + log_file_name)
                os.makedirs(directory, exist_ok=True)
                fh = logging.FileHandler(processing_data + "/" + log_file_name, mode="a")
                fh.setFormatter(formatter)
                fh.setLevel(log_level)
                mylogger.addHandler(fh)
    else:
        print("ERROR: Logger not initialisable.")
    return mylogger


# just log every occurance
def log_all(log_level,key, message):
    global mylogger
    global general_log_level
    global main_log_file
    if mylogger==None:
        mylogger = prepare_logger(general_log_level,main_log_file)
    mylogger.log(log_level,key+": "+message)

# Only prints the message once and continues
def log_once(log_level,key,message):
    global log_dict
    global mylogger
    if mylogger==None:
        mylogger = prepare_logger(general_log_level,main_log_file)
    a = log_dict.get(key)
    if a == None:
        log_dict[key]=[1,message]
        mylogger.log(log_level,key+":" +message)
    else:
        count=log_dict[key][0]
        mess=log_dict[key][1]
        log_dict[key]=[count,mess]

# writes the numbers of occurances of each error type
def log_write_counts(log_level):
    global log_dict
    global mylogger
    if mylogger==None:
        mylogger = prepare_logger(general_log_level,main_log_file)
    if len(log_dict)>0:
        mylogger.log(logging.INFO,'Logging: Recapitulation of warnings')
        for key, arr in log_dict.items():
            mylogger.log(log_level, f'{key}: {arr[1]} (counted {arr[0]})')
        log_dict = {}
        log_flush()


# flushes the log to disk
def log_flush():
    global mylogger
    if not mylogger==None:
        for handler in mylogger.handlers:
            handler.flush()
    else:
        print("ERROR: not flushing log.")



