#  We will have logging based on the standard logging
# https://docs.python.org/3/howto/logging.html
# --log=INFO
# --logfile=filename

import logging

NOSOFTLOGGING=False

# Basic ideas:
# - There might still remain print statements, that are just send to the screen
# - we still wrap them to make sure, we can deactivate it
# - log level can be set
# - There is a standard log (log format)
# - Some logs have special purposes (e.g. the script protocol, outputs with lists)
# - some things are corrected and only one problem is resolved.
# - the logging should assist the pipeline.

def log_print(s):
    if not NOSOFTLOGGING:
        print(s)

def prepare_logger(log_level,log_file_name,module_name):
    # create logger
    logger = logging.getLogger(module_name)
    logger.setLevel(log_level)

    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # add formatter to ch
    ch.setFormatter(formatter)

    # add ch to logger
    logger.addHandler(ch)
    fh = logging.FileHandler(log_file_name)
    fh.setFormatter(formatter)
    fh.setLevel(log_level)
    logger.addHandler(fh)
    return logger

