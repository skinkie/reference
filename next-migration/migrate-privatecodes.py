import lxml
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.handlers import LxmlEventHandler
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from netex import Operator, PrivateCodes, PrivateCode, FareScheduledStopPoint, InterchangeRule, \
    LineInDirectionRefStructure, ScheduledStopPoint

ns_map={'': 'http://www.netex.org.uk/netex', 'gml': 'http://www.opengis.net/gml/3.2'}

import glob

def applyOperator(o: Operator):
    private_codes = []

    if o.private_code is not None:
        private_codes.append(o.private_code)

    if o.external_operator_ref is not None:
        private_codes.append(PrivateCode(type_value=o.external_operator_ref.type_value, value=o.external_operator_ref.ref.strip()))

    if len(private_codes) > 0:
        o.private_codes = PrivateCodes(private_code=private_codes)
        o.private_code = None
        o.external_operator_ref = None

    return o


def applyFareScheduledStopPoint(f: FareScheduledStopPoint):
    private_codes = []

    if f.private_code is not None:
        private_codes.append(f.private_code)

    if f.external_stop_point_ref is not None:
        private_codes.append(
            PrivateCode(type_value=f.external_stop_point_ref.type_value, value=f.external_stop_point_ref.ref.strip()))

    if len(private_codes) > 0:
        f.private_codes = PrivateCodes(private_code=private_codes)
        f.private_code = None
        f.external_stop_point_ref = None

    return f

def applyScheduledStopPoint(f: ScheduledStopPoint):
    private_codes = []

    if f.private_code is not None:
        private_codes.append(f.private_code)

    if f.external_stop_point_ref is not None:
        if f.external_stop_point_ref.type_value == None or f.external_stop_point_ref.type_value == '':
            f.external_stop_point_ref.type_value = 'ExternalStopPointRef'

        private_codes.append(
            PrivateCode(type_value=f.external_stop_point_ref.type_value, value=f.external_stop_point_ref.ref.strip()))

    if len(private_codes) > 0:
        f.private_codes = PrivateCodes(private_code=private_codes)
        f.private_code = None
        f.external_stop_point_ref = None

    return f

def conversion(input_filename):
    serializer_config = SerializerConfig(ignore_default_attributes=True)
    # serializer_config.pretty_print = True
    # serializer_config.ignore_default_attributes = True
    serializer = XmlSerializer(serializer_config)

    context = XmlContext()
    config = ParserConfig(fail_on_unknown_properties=False)
    parser = XmlParser(context=context, config=config, handler=LxmlEventHandler)


    p= lxml.etree.XMLParser(remove_blank_text=True)
    tree = lxml.etree.parse(input_filename, parser=p)
    # for element in tree.iterfind(".//{http://www.netex.org.uk/netex}Operator"):
    #     element.getparent().replace(element, lxml.etree.fromstring(serializer.render(applyOperator(parser.parse(element, Operator)), ns_map).encode('utf-8'), p))

    for element in tree.iterfind(".//{http://www.netex.org.uk/netex}FareScheduledStopPoint"):
        element.getparent().replace(element, lxml.etree.fromstring(serializer.render(applyFareScheduledStopPoint(parser.parse(element, FareScheduledStopPoint)), ns_map).encode('utf-8'), p))

    for element in tree.iterfind(".//{http://www.netex.org.uk/netex}ScheduledStopPoint"):
        element.getparent().replace(element, lxml.etree.fromstring(serializer.render(applyScheduledStopPoint(parser.parse(element, ScheduledStopPoint)), ns_map).encode('utf-8'), p))

    for element in tree.iterfind(".//*"):
        if element.text is None and len(element) == 0 and len(element.attrib.keys()) == 0:
            element.getparent().remove(element)

    tree.write(input_filename)

if __name__ == '__main__':
    for input_filename in glob.glob("/home/skinkie/Sources/NeTEx/examples/standards/vdv452/timetable/*.xml"):
        print(input_filename)
        conversion(input_filename)





# LineInDirectionRefStructure()

# InterchangeRule()