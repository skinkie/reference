from dataclasses import dataclass, field
from netex.vehicle_service_place_assignment_version_structure import VehicleServicePlaceAssignmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleServicePlaceAssignment1(VehicleServicePlaceAssignmentVersionStructure):
    """The allocation of a place to a MOBILITY SERVICE.

    +V1.2.2

    :ivar id: Identifier of ENTITY.
    """
    class Meta:
        name = "VehicleServicePlaceAssignment"
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
