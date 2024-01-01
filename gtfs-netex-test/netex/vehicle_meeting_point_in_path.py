from dataclasses import dataclass
from .vehicle_meeting_point_in_path_version_structure import (
    VehicleMeetingPointInPathVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleMeetingPointInPath(VehicleMeetingPointInPathVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
