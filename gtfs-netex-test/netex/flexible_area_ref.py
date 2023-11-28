from dataclasses import dataclass
from netex.flexible_area_ref_structure import FlexibleAreaRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FlexibleAreaRef(FlexibleAreaRefStructure):
    """
    Reference to a FLEXIBLE AREA.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
