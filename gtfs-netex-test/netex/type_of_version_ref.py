from dataclasses import dataclass
from .type_of_version_ref_structure import TypeOfVersionRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfVersionRef(TypeOfVersionRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
