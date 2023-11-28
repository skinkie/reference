from dataclasses import dataclass
from netex.stop_event_request_ref_structure import StopEventRequestRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class StopEventRequestRef(StopEventRequestRefStructure):
    """
    Reference to a STOP EVENT REQUEST.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
