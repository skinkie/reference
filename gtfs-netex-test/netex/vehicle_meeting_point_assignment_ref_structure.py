from dataclasses import dataclass
from netex.assignment_ref_structure import AssignmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleMeetingPointAssignmentRefStructure(AssignmentRefStructure):
    """
    Type for a reference to a VEHICLE MEETING POINT ASSIGNMENT.
    """
