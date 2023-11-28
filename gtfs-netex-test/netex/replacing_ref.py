from dataclasses import dataclass
from netex.replacing_ref_structure import ReplacingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ReplacingRef(ReplacingRefStructure):
    """
    Reference to a REPLACING PARAMETER.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
