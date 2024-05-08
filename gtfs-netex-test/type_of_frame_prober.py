import glob
from xsdata.formats.dataclass.parsers.handlers import lxml


def prober(path: str):
    skip_xml = False
    for input_filename in glob.glob(path):
        ref = None
        if not skip_xml:
            tree = lxml.etree.parse(input_filename)
            for type_of_frame_ref in tree.iterfind(".//{http://www.netex.org.uk/netex}TypeOfFrameRef"):
                ref = type_of_frame_ref.attrib['ref']

        if ref is None and 'SCHWEIZ_' in input_filename:
            skip_xml = True
            if 'SCHWEIZ_COMMON_' in input_filename:
                ref = 'ch:TypeOfFrame:COMMON'
            elif 'SCHWEIZ_RESOURCE_' in input_filename:
                ref = 'ch:TypeOfFrame:RESOURCE'
            elif 'SCHWEIZ_SERVICE_' in input_filename:
                ref = 'ch:TypeOfFrame:SERVICE'
            elif 'SCHWEIZ_SERVICECALENDAR_' in input_filename:
                ref = 'ch:TypeOfFrame:SERVICECALENDAR'
            elif 'SCHWEIZ_SITE_' in input_filename:
                ref = 'ch:TypeOfFrame:SITE'
            elif 'SCHWEIZ_TIMETABLE_' in input_filename:
                ref = 'ch:TypeOfFrame:TIMETABLE'

        print(input_filename, ref, ref in type_of_frames)

if __name__ == '__main__':
    prober("/home/netex/sbb/*.xml")