from dataclasses import dataclass
from .vehicle_type_stop_assignment_version_structure import (
    VehicleTypeStopAssignmentVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleTypeStopAssignment(VehicleTypeStopAssignmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
