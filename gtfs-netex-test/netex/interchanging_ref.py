from dataclasses import dataclass
from netex.interchanging_ref_structure import InterchangingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class InterchangingRef(InterchangingRefStructure):
    """
    Reference to a INTERCHANGING.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
