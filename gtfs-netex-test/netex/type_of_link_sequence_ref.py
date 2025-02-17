from dataclasses import dataclass

from .type_of_link_sequence_ref_structure import TypeOfLinkSequenceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TypeOfLinkSequenceRef(TypeOfLinkSequenceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
