from dataclasses import dataclass, field
from typing import Optional

from .type_of_fuel_enumeration import TypeOfFuelEnumeration
from .type_of_value_structure import TypeOfValueStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class TypeOfVehicleFuelStructure:
    type_of_fuel: TypeOfFuelEnumeration = field(
        metadata={
            "name": "TypeOfFuel",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    other_type_of_fuel: Optional[TypeOfValueStructure] = field(
        default=None,
        metadata={
            "name": "OtherTypeOfFuel",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
