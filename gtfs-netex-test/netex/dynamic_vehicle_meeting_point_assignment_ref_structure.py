from dataclasses import dataclass
from .vehicle_meeting_point_assignment_ref_structure import (
    VehicleMeetingPointAssignmentRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DynamicVehicleMeetingPointAssignmentRefStructure(
    VehicleMeetingPointAssignmentRefStructure
):
    value: RestrictedVar
