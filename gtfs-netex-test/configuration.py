# CONFIGURATION:
import logging
# Logging
log_dict={}  # relevant values key - type of problem, then  [count, message]
NOSOFTLOGGING=False  # if set to True the log_print function will output nothing
LOGEXAMPLE=False # if set to True then tool_check_db will print a random row for each table
general_log_level = logging.INFO



main_log_file = "aux.log" # in the processing_data folder

# FrameDefaults
defaults = {}
defaults["authority"]= "http://openov.nl/"
defaults["timezone"]= "Europe/Amsterdam"
defaults["particpant_ref"] = "NDOV"
defaults["xml_description"] = "Huge XML Serializer test"
defaults["feed_publisher_name"]= "Publication Delivery"
defaults["feed_publisher_url"]= "http://publicationdelivery.eu"
defaults["os"]= "windows"
defaults["authority_reference"] = True
input_dir = "d:/input"
processing_data =  "d:/aux_testing_processing"

# a local configuration overwrites the general one. The local_configuration must not be added to github
try:
    from local_configuration import *
except:
    pass
