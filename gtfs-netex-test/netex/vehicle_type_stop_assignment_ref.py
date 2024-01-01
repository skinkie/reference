from dataclasses import dataclass
from .vehicle_type_stop_assignment_ref_structure import (
    VehicleTypeStopAssignmentRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleTypeStopAssignmentRef(VehicleTypeStopAssignmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
