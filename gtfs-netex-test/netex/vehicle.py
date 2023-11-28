from dataclasses import dataclass, field
from netex.vehicle_version_structure import VehicleVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class Vehicle(VehicleVersionStructure):
    """
    A public transport vehicle used for carrying passengers.

    :ivar id: Identifier of VEHICLE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
