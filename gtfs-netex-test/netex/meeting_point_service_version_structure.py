from dataclasses import dataclass, field
from typing import Optional
from netex.customer_service_version_structure import CustomerServiceVersionStructure
from netex.meeting_point_enumeration import MeetingPointEnumeration
from netex.multilingual_string import MultilingualString

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class MeetingPointServiceVersionStructure(CustomerServiceVersionStructure):
    """
    Type for a MEETING POINT SERVICE.

    :ivar meeting_point_service_type: Type of MEETING POINT.
    :ivar label: Label of meeting point.
    """
    class Meta:
        name = "MeetingPointService_VersionStructure"

    meeting_point_service_type: MeetingPointEnumeration = field(
        metadata={
            "name": "MeetingPointServiceType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    label: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Label",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
