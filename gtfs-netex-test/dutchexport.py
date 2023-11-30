from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.models.datatype import XmlDateTime

from dutchprofile import DutchProfile
from netex import Codespace, Version, VersionTypeEnumeration, DataSource, MultilingualString, ResponsibilitySet, \
    ResponsibilityRoleAssignmentsRelStructure, ResponsibilityRoleAssignment, VersionOfObjectRefStructure
import datetime

from refs import getId

ns_map = {'': 'http://www.netex.org.uk/netex', 'gml': 'http://www.opengis.net/gml/3.2'}

short_name = "TESO"

codespace = Codespace(id="{}:Codespace:{}".format(short_name, short_name), xmlns=short_name,
                      xmlns_url="https://teso.nl/", description=short_name)

start_date = datetime.datetime(year=2023, month=11, day=29)
end_date = datetime.datetime(year=2023, month=12, day=29)

version = Version(id=getId(Version, codespace, str(1)),
                  version=str(1),
                  start_date=XmlDateTime.from_datetime(start_date),
                  end_date=XmlDateTime.from_datetime(end_date),
                  version_type=VersionTypeEnumeration.BASELINE)

data_source = DataSource(id=getId(DataSource, codespace, short_name),
                         version=version.version,
                         name=MultilingualString(value=short_name),
                         short_name=MultilingualString(value=short_name),
                         description=MultilingualString(value=short_name))

responsibility_set = ResponsibilitySet(id=getId(ResponsibilitySet, codespace, short_name),
                                       version=version.version,
                                       name=MultilingualString(value=short_name),
                                       roles=ResponsibilityRoleAssignmentsRelStructure(responsibility_role_assignment=[
                                           ResponsibilityRoleAssignment(id=getId(ResponsibilityRoleAssignment, codespace, "TESO"),
                                                                        version=version.version,
                                                                        data_role_type=None,
                                                                        stakeholder_role_type=None,
                                                                        responsible_area_ref=VersionOfObjectRefStructure(ref="NL:TransportAdministrativeZone:TESO", version="any", name_of_ref_class="TransportAdministrativeZone"))
                                       ]))

dutchprofile = DutchProfile(codespace, data_source, responsibility_set, version)
resource_frames = dutchprofile.getResourceFrames(data_sources=[data_source], responsibility_sets=[responsibility_set])
composite_frame = dutchprofile.getCompositeFrame(resource_frames=resource_frames)
publication_delivery = dutchprofile.getPublicationDelivery(composite_frame=composite_frame, description="Eerste TESO export")

serializer_config = SerializerConfig(ignore_default_attributes=True)
serializer_config.pretty_print = True
serializer_config.ignore_default_attributes = True
serializer = XmlSerializer(serializer_config)

with open('netex-output/out.xml', 'w') as out:
    serializer.write(out, publication_delivery, ns_map)