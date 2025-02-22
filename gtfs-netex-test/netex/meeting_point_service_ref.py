from dataclasses import dataclass

from .meeting_point_service_ref_structure import MeetingPointServiceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class MeetingPointServiceRef(MeetingPointServiceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
