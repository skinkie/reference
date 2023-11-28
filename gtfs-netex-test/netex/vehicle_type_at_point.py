from dataclasses import dataclass, field
from netex.vehicle_type_at_point_version_structure import VehicleTypeAtPointVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleTypeAtPoint(VehicleTypeAtPointVersionStructure):
    """NETWORK RESTRICTION.

    specifying whether a vehicle of a specified VEHICLE TYPE may visit a
    point.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
