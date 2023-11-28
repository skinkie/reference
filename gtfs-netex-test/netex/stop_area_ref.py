from dataclasses import dataclass
from netex.stop_area_ref_structure import StopAreaRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class StopAreaRef(StopAreaRefStructure):
    """
    Reference to a STOP AREA.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
