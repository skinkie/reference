from dataclasses import dataclass
from netex.submode_ref_structure import SubmodeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SubmodeRef(SubmodeRefStructure):
    """
    Reference to a SUBMODE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
