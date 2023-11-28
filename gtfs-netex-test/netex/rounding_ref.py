from dataclasses import dataclass
from netex.rounding_ref_structure import RoundingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RoundingRef(RoundingRefStructure):
    """
    Reference to a ROUNDING.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
