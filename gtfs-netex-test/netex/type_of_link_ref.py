from dataclasses import dataclass
from .type_of_link_ref_structure import TypeOfLinkRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfLinkRef(TypeOfLinkRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
