from dataclasses import dataclass, field
from netex.vehicle_type_zone_restriction_version_structure import VehicleTypeZoneRestrictionVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleTypeZoneRestriction(VehicleTypeZoneRestrictionVersionStructure):
    """A POINT where passengers can board or alight from vehicles.

    +v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
