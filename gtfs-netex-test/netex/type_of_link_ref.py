from dataclasses import dataclass
from netex.type_of_link_ref_structure import TypeOfLinkRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfLinkRef(TypeOfLinkRefStructure):
    """
    Reference to a TYPE OF LINK.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
