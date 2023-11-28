from dataclasses import dataclass
from netex.stop_finder_request_ref_structure import StopFinderRequestRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class StopFinderRequestRef(StopFinderRequestRefStructure):
    """
    Reference to a STOP FINDER REQUEST.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
