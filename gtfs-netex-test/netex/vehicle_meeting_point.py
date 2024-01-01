from dataclasses import dataclass
from .vehicle_meeting_point_version_structure import (
    VehicleMeetingPointVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleMeetingPoint(VehicleMeetingPointVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
