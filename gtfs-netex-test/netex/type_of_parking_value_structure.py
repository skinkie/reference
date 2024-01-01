from dataclasses import dataclass
from .type_of_value_version_structure import TypeOfValueVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfParkingValueStructure(TypeOfValueVersionStructure):
    class Meta:
        name = "TypeOfParking_ValueStructure"
