from dataclasses import dataclass
from netex.access_space_ref_structure import AccessSpaceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AccessSpaceRef(AccessSpaceRefStructure):
    """
    Reference to an ACCESS SPACE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
