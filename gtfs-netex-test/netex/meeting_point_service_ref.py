from dataclasses import dataclass
from netex.meeting_point_service_ref_structure import MeetingPointServiceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class MeetingPointServiceRef(MeetingPointServiceRefStructure):
    """
    Identifier of an MEETING POINT SERVICE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
