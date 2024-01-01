from dataclasses import dataclass
from .vehicle_type_zone_restriction_version_structure import (
    VehicleTypeZoneRestrictionVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleTypeZoneRestriction(VehicleTypeZoneRestrictionVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
