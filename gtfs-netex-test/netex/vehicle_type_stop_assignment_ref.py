from dataclasses import dataclass
from netex.vehicle_type_stop_assignment_ref_structure import VehicleTypeStopAssignmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleTypeStopAssignmentRef(VehicleTypeStopAssignmentRefStructure):
    """
    Reference to a VEHICLE TYPE STOP ASSIGNMENT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
