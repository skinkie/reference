from dataclasses import dataclass
from netex.stop_assignment_ref_structure import StopAssignmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleTypeStopAssignmentRefStructure(StopAssignmentRefStructure):
    """
    Type for a reference to a VEHICLE TYPE STOP ASSIGNMENT.
    """
