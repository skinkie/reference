from dataclasses import dataclass
from .vehicle_type_zone_restriction_ref_structure import (
    VehicleTypeZoneRestrictionRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleTypeZoneRestrictionRef(VehicleTypeZoneRestrictionRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
