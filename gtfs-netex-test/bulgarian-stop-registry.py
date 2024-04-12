from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.models.datatype import XmlDateTime
import datetime

from netex import StopPlace, StatusEnumeration, MultilingualString, AlternativeNamesRelStructure, AlternativeName, \
    Codespace, NameTypeEnumeration, StopTypeEnumeration, SimplePointVersionStructure, LocationStructure2, Extensions2, \
    QuaysRelStructure, Quay, PrivateCode, InfoLinksRelStructure, InfoLink, SiteFrame, \
    StopPlacesInFrameRelStructure, PublicationDelivery, DataObjectsRelStructure, CompositeFrame, FramesRelStructure, \
    CodespacesRelStructure, AllVehicleModesOfTransportEnumeration
from refs import getId

CREDENTIALS = "/home/skinkie/Downloads/bulgarian-stop-registry-3be3e77d8290.json"

import pygsheets
import pandas as pd
#authorization
gc = pygsheets.authorize(service_file=CREDENTIALS)

#open the google spreadsheet (where 'PY to Gsheet Test' is the name of my sheet)
sh = gc.open('BSR Master')

#select the first sheet
wks = sh[0]

version = str(1) # Do something more elegant

codespace = Codespace(id="BSR:Codespace:BSR", xmlns="BSR", xmlns_url="http://tripco.bg")

def get_alternative_names(numeral, codespace, row):

    """
    'cyrillic_name': 'Училище Йордан Йовков',
    'local_name': '', 'google_translate': 'Jordan Yovkov School', 'latin_name': 'Uciliste Jordan Jovkov',
    'english_name': 'Yordan Yovkov School', 'name_comment': '', 'cyrillic_abbr': '', 'latin_abbr': '',
    'english_abbr': '', 'cyrillic_alternative_name': '', 'latin_alternative_name': '', 'english_alternative_name': '',
        """
    ans = []
    if row['cyrillic_name'] != '':
        an = AlternativeName(lang="bg",
                             name_type=NameTypeEnumeration.COPY, name=MultilingualString(value=row['cyrillic_name']))
        if row['cyrillic_abbr'] != '':
            an.abbreviation = MultilingualString(value=row['cyrillic_abbr'])
        ans.append(an)

    if row['latin_name'] != '':
        an = AlternativeName(lang="bg",
                             name_type=NameTypeEnumeration.COPY, name=MultilingualString(value=row['latin_name']))
        if row['latin_abbr'] != '':
            an.abbreviation = MultilingualString(value=row['latin_abbr'])
        ans.append(an)

    if row['english_name'] != '':
        an = AlternativeName(lang="en",
                             name_type=NameTypeEnumeration.TRANSLATION, name=MultilingualString(value=row['english_name']))
        if row['english_abbr'] != '':
            an.abbreviation = MultilingualString(value=row['english_abbr'])
        ans.append(an)

    if len(ans) > 0:
        return AlternativeNamesRelStructure(alternative_name=ans)

def get_description(row):
    descs = []
    if row['cyrillic_stopplace_description'] != '':
        descs.append(MultilingualString(lang="bg", value=row['cyrillic_stopplace_description']))

    elif row['latin_stopplace_description'] != '':
        descs.append(MultilingualString(lang="bg", value=row['latin_stopplace_description']))

    elif row['english_stopplace_description'] != '':
        descs.append(MultilingualString(lang="en", value=row['english_stopplace_description']))

    if len(descs) > 0:
        return descs

def empty_is_none(value):
    if value != '':
        return value

def get_stop_type(value):
    if value != '':
        return StopTypeEnumeration(value)

def get_transport_mode(value):
    if value:
        return AllVehicleModesOfTransportEnumeration(value)

def get_stop_places():
    return [StopPlace(
            id=getId(StopPlace, codespace, row['numeral']),
            version=version,
            status_attribute=StatusEnumeration(row['lifecycle']),
            name=MultilingualString(value=row['cyrillic_name']),
            alternative_names=get_alternative_names(row['numeral'], codespace, row),
            description=get_description(row),
            stop_place_type=get_stop_type(row['stopPlaceType']),
            centroid=SimplePointVersionStructure(location=LocationStructure2(latitude=row['lat'], longitude=row['lon'])),
            quays=QuaysRelStructure(taxi_stand_ref_or_quay_ref_or_quay=[Quay(
                id=getId(Quay, codespace, row['numeral']),
                version=version,
                name=MultilingualString(value=row['cyrillic_name']),
                alternative_names=get_alternative_names(row['numeral'], codespace, row),
                centroid=SimplePointVersionStructure(location=LocationStructure2(latitude=row['lat'], longitude=row['lon'])),
                private_code=PrivateCode(value=row['quay privateCode']),
                public_code=empty_is_none(row['quay publicCode'])
            )]),
            transport_mode=get_transport_mode(row['mode']),
            info_links=InfoLinksRelStructure(info_link=[InfoLink(value=row['google maps link'], type_of_info_link=[TypeOfInfolinkEnumeration.MAP])]),
            extensions=Extensions2(any_element=[AnyElement(qname="{http://www.netex.org.uk/netex}Source", text=row['source'])]),
        ) for row in wks.get_all_records()]

site_frame = SiteFrame(id=getId(SiteFrame, codespace, "1"), version="1",
                          stop_places=StopPlacesInFrameRelStructure(stop_place=get_stop_places())
                          )

publication_delivery = PublicationDelivery(participant_ref="PyNeTExConv",
                                           publication_timestamp=XmlDateTime.from_datetime(datetime.datetime.now()))
publication_delivery.version = "ntx:1.1"
publication_delivery.description = "NeTEx export"
publication_delivery.data_objects = DataObjectsRelStructure(choice=[site_frame])
"""    
    CompositeFrame(
    id=getId(CompositeFrame, codespace, "1"),
    version="1",
    codespaces=CodespacesRelStructure(codespace_ref_or_codespace=[codespace]),
    frames=FramesRelStructure(common_frame=[site_frame]))])
"""

serializer_config = SerializerConfig(ignore_default_attributes=True)
serializer_config.pretty_print = True
serializer_config.ignore_default_attributes = True
serializer = XmlSerializer(config=serializer_config)

ns_map = {None: 'http://www.netex.org.uk/netex', 'gml': 'http://www.opengis.net/gml/3.2'}

serializer.write(open('/tmp/bsr.xml', 'w'), publication_delivery, ns_map)
