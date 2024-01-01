from dataclasses import dataclass
from .type_of_projection_ref_structure import TypeOfProjectionRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfProjectionRef(TypeOfProjectionRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
