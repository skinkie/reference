from dataclasses import dataclass, field
from netex.vehicle_type_version_structure import VehicleTypeVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleType(VehicleTypeVersionStructure):
    """
    A classification of public transport vehicles according to the vehicle
    scheduling requirements in mode and capacity (e.g. standard bus, double-deck,
    ...).

    :ivar id: Identifier of VEHICLE TYPE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
