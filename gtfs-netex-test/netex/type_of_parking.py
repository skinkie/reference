from dataclasses import dataclass
from .type_of_parking_value_structure import TypeOfParkingValueStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfParking(TypeOfParkingValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
