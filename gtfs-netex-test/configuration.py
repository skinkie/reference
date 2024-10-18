# CONFIGURATION:
import logging
# Logging
log_dict={}  # relevant values key - type of problem, then  [count, message]
mylogger = None  # the main logger
NOSOFTLOGGING=False  # if set to True the log_print function will output nothing
general_log_level = logging.INFO

# Basic files for script runner
processing_data = "d:/aux_testing_processing"
# processing_data = "C:/Users/ue71603/MG_Daten/github/reference1/gtfs-netex-test/aux_test_processing"

main_log_file = "aux.log" # in the processing_data folder

# a local configuration overwrites the general one. The local_configuration must not be added to github
try:
    from local_configuration import *
except:
    pass