from dataclasses import dataclass
from netex.type_of_parking_ref_structure import TypeOfParkingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfParkingRef(TypeOfParkingRefStructure):
    """
    Reference to a TYPE OF PARKING.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
