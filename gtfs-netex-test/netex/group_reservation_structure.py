from dataclasses import dataclass, field

from .natural_language_string_structure import NaturalLanguageStringStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupReservationStructure:
    name_of_group: NaturalLanguageStringStructure = field(
        metadata={
            "name": "NameOfGroup",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    number_of_reserved_seats: int = field(
        metadata={
            "name": "NumberOfReservedSeats",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
