from dataclasses import dataclass
from netex.vehicle_type_zone_restriction_ref_structure import VehicleTypeZoneRestrictionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleTypeZoneRestrictionRef(VehicleTypeZoneRestrictionRefStructure):
    """Reference to an VEHICLE TYPE ZONE RESTRICTION.

    +v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
