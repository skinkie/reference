from dataclasses import dataclass
from .type_of_line_ref_structure import TypeOfLineRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfLineRef(TypeOfLineRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
