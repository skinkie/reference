from dataclasses import dataclass
from netex.access_ref_structure import AccessRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AccessRef(AccessRefStructure):
    """
    Reference to an ACCESS link.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
