from dataclasses import dataclass
from .vehicle_meeting_point_assignment_version_structure import (
    VehicleMeetingPointAssignmentVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleMeetingPointAssignment1(
    VehicleMeetingPointAssignmentVersionStructure
):
    class Meta:
        name = "VehicleMeetingPointAssignment"
        namespace = "http://www.netex.org.uk/netex"
