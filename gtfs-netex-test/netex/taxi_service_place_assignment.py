from dataclasses import dataclass, field
from netex.taxi_service_place_assignment_version_structure import TaxiServicePlaceAssignmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TaxiServicePlaceAssignment(TaxiServicePlaceAssignmentVersionStructure):
    """The allocation of a TAXI SERVICE to a TAXI PARKING or a TAXI STAND.

    +V1.2.2

    :ivar id: Identifier of ENTITY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
