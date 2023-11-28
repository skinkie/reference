from dataclasses import dataclass, field
from netex.vehicle_sharing_mode_of_operation_value_structure import VehicleSharingModeOfOperationValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleSharing(VehicleSharingModeOfOperationValueStructure):
    """Short term VEHICLE RENTAL where the vehicle can be taken from and parked at
    different places in the urban area, possibly without the constraint to bring
    back the vehicle to a specific location.

    +v1.2.2

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
