from dataclasses import dataclass, field

from .natural_language_string_structure import NaturalLanguageStringStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class GroupReservationStructure:
    name_of_group: NaturalLanguageStringStructure = field(
        metadata={
            "name": "NameOfGroup",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    number_of_reserved_seats: int = field(
        metadata={
            "name": "NumberOfReservedSeats",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
