# Programs reads a file and returns information about a lot of elements
import xml.etree.ElementTree as ET

# elements to count
elementlist = ['ResourceFrame','ResponsibilitySet','Notice','TypeofProductCategory','AlternativeText','AlternativeName','ServiceCalendarFrame','DayType','DayTypeAssignment','Organisation',
 'Operator','Authority','SiteFrame','StopPlace','Quay','ServiceFrame','Direction','Network','Line','GroupOfLines','DefaultConnection','AvailabilityCondition','ScheduledStopPoint','StopArea','TariffZone',
 'ServiceLink','PassengerStopAssignment','ServiceJourneyPattern','TimetableFrame','ServiceJourney','Call','JourneyMeeting','CoupledJourney','JourneyPart','InterchangeRule','AccessibilityAssessment','CheckConstraint','TemplateServiceJourney']

def get_element_names(node):
    element_names = []
    for child in node:
        element_names.append(child.tag)
        element_names.extend(get_element_names(child))
    return element_names

def main(file: str):
    print("***************************************************")
    print("file: "+file)
    print("***************************************************")

    tree=ET.parse(file)
    print(tree)
    rt=tree.getroot()

    # Get the element names of all nodes
    element_names = get_element_names(rt)

    # Print the list of element names
    #print("All element types found:")
    #for name in element_names:
    #    print(name)
    print("***************************************************")

    for el in elementlist:
        srch= ".//{http://www.netex.org.uk/netex}"+el
        res=rt.findall(srch)
        if not(res == None):
            if (len(res)>0):
                print (el +": "+str(len(res)))

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='NeTEx statistics')
    parser.add_argument('file', type=str, help='NeTEx file to process')
    args = parser.parse_args()

    main(args.file)