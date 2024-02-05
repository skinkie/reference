from typing import List

from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.handlers import LxmlEventHandler

import lxml

from gtfsprofile import GtfsProfile
from netex import Line


def convert(input_filename: str):
    context = XmlContext()
    config = ParserConfig(fail_on_unknown_properties=False)
    parser = XmlParser(context=context, config=config, handler=LxmlEventHandler)

    tree = lxml.etree.parse(input_filename)

    # lines: List[Line] = []

    for element in tree.iterfind(".//{http://www.netex.org.uk/netex}Line"):
        line: Line = parser.parse(element, Line)
        GtfsProfile.projectLineToRoute(line)


    # TODO: GTFS does not support Branding, so in order to facilitate it we will make it a separate Agency

