#  We will have logging based on the standard logging
# https://docs.python.org/3/howto/logging.html
# --log=INFO
# --logfile=filename

import logging
log_dict={}
mylogger = None
NOSOFTLOGGING=False
general_log_level = logging.WARNING

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

def prepare_logger(log_level,log_file_name,module_name):
    # create logger
    global mylogger
    global log_dict
    if not mylogger:
        mylogger = logging.getLogger(module_name)
    mylogger.setLevel(log_level)
    log_dict ={}
    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # add formatter to ch
    ch.setFormatter(formatter)
    mylogger.addHandler(ch)

    # add ch to logger
    if not log_file_name==None and len(log_file_name)>5:
        fh = logging.FileHandler(log_file_name,mode="a")
        fh.setFormatter(formatter)
        fh.setLevel(log_level)
        mylogger.addHandler(fh)
    return mylogger


# just log every occurance
def log_all(log_level,key, message):
    global mylogger
    global general_log_level
    if mylogger==None:
        mylogger = prepare_logger(general_log_level,message,key)
    mylogger.log(log_level,key+": "+message)

# Only prints the message once and continues
def log_once(log_level,key,message):
    global log_dict
    global mylogger
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
    for key,arr in log_dict.items():
        mylogger.log(log_level,key,f'{arr[1]} (counted {arr[0]}')
    log_dict={}
    log_flush()

# flushes the log to disk
def log_flush():
    global mylogger
    if not mylogger==None:
        for handler in mylogger.handlers:
            handler.flush()


