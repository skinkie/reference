from dataclasses import dataclass, field
from netex.vehicle_pooling_place_assignment_version_structure import VehiclePoolingPlaceAssignmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehiclePoolingPlaceAssignment(VehiclePoolingPlaceAssignmentVersionStructure):
    """The allocation of a VEHICLE POOLING SERVICE to a VEHICLE POOLING PARKING
    AREA or a VEHICLE POOLING MEETING PLACE.

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
