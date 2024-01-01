from dataclasses import dataclass
from .type_of_plug_ref_structure import TypeOfPlugRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfPlugRef(TypeOfPlugRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
