from dataclasses import dataclass
from .vehicle_type_at_point_version_structure import (
    VehicleTypeAtPointVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleTypeAtPoint(VehicleTypeAtPointVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
