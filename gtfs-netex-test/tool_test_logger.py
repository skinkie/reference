# Programs reads a file and returns information about a lot of elements
import argparse
import logging
import traceback

from aux_logging import *
import xml.etree.ElementTree as ET

# elements to count and report in the statistics
elementlist = ['ResourceFrame','ResponsibilitySet','Notice','TypeofProductCategory','AlternativeText','AlternativeName','ServiceCalendarFrame','DayType','DayTypeAssignment','Organisation',
 'Operator','Authority','SiteFrame','StopPlace','Quay','ServiceFrame','Direction','Network','Line','GroupOfLines','DefaultConnection','AvailabilityCondition','ScheduledStopPoint','StopArea','TariffZone',
 'ServiceLink','PassengerStopAssignment','ServiceJourneyPattern','TimetabledPassingTime','TimetableFrame','ServiceJourney','Call','JourneyMeeting','CoupledJourney','JourneyPart','InterchangeRule','AccessibilityAssessment','CheckConstraint','TemplateServiceJourney','ServiceFacilitySet','UicOperatingPeriod']

def get_element_names(node):
    element_names = []
    for child in node:
        element_names.append(child.tag)
        element_names.extend(get_element_names(child))
    return element_names

def main(log_file:str):
    global mylogger
    global processing_data
    if log_file == None:
        log_file="stats.log"
    log_print("***************************************************")
    log_all(logging.INFO,"mess1")
    log_once(logging.INFO,"keyINFOOnce","mess2")
    log_once(logging.INFO,"keyINFOOnce","mess3")
    log_once(logging.INFO,"keyINFOOnce","mess4")
    log_once(logging.INFO,"keyINFOOnce","mess5")
    log_once(logging.WARN,"keyINFOOnce2","mess6")
    log_once(logging.INFO,"keyINFOOnce","mess7")
    log_once(logging.ERROR,"keyINFOOnce2","mess8")
    raise Exception("Exception raised")



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='NeTEx statistics')
    parser.add_argument('--log_file', type=str, required=False,
                 help='the logfile')
    args = parser.parse_args()
    mylogger = prepare_logger(logging.INFO, args.log_file)
    mylogger = prepare_logger(logging.INFO, args.log_file)
    mylogger = prepare_logger(logging.INFO, args.log_file)
    mylogger = prepare_logger(logging.INFO, args.log_file)
    try:
        main(args.log_file)
    except Exception as e:
        log_all(logging.ERROR, f'{e} {traceback.format_exc()}')
    log_write_counts(logging.INFO)
