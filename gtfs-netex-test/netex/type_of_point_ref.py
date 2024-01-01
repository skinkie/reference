from dataclasses import dataclass
from .type_of_point_ref_structure import TypeOfPointRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfPointRef(TypeOfPointRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
