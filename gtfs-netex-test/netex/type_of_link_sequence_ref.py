from dataclasses import dataclass
from netex.type_of_link_sequence_ref_structure import TypeOfLinkSequenceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfLinkSequenceRef(TypeOfLinkSequenceRefStructure):
    """
    Reference to a TYPE OF LINK SEQUENCE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
