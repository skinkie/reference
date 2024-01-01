from dataclasses import dataclass
from .type_of_version_value_structure import TypeOfVersionValueStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfVersion(TypeOfVersionValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
