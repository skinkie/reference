from dataclasses import dataclass
from netex.schedule_request_ref_structure import ScheduleRequestRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ScheduleRequestRef(ScheduleRequestRefStructure):
    """
    Reference to a SCHEDULE REQUEST.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
