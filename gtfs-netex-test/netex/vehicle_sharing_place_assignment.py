from dataclasses import dataclass, field
from netex.vehicle_sharing_place_assignment_version_structure import VehicleSharingPlaceAssignmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleSharingPlaceAssignment(VehicleSharingPlaceAssignmentVersionStructure):
    """The allocation of a VEHICLE SHARING AREA to any vehicle sharing or rental
    service.

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
