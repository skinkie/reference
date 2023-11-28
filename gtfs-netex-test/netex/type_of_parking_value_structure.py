from dataclasses import dataclass
from netex.type_of_value_version_structure import TypeOfValueVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfParkingValueStructure(TypeOfValueVersionStructure):
    """
    Type for a TYPE OF PARKING.
    """
    class Meta:
        name = "TypeOfParking_ValueStructure"
