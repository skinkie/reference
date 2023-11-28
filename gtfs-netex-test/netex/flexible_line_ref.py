from dataclasses import dataclass
from netex.flexible_line_ref_structure import FlexibleLineRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FlexibleLineRef(FlexibleLineRefStructure):
    """
    Reference to a FLEXIBLE LINE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
