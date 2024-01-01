from dataclasses import dataclass
from .type_of_link_sequence_ref_structure import TypeOfLinkSequenceRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfLinkSequenceRef(TypeOfLinkSequenceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
