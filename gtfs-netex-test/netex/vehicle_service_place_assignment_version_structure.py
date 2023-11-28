from dataclasses import dataclass
from netex.assignment_version_structure_1 import AssignmentVersionStructure1

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleServicePlaceAssignmentVersionStructure(AssignmentVersionStructure1):
    """
    Type for VEHICLE SERVICE PLACE ASSIGNMENT restricts id.
    """
    class Meta:
        name = "VehicleServicePlaceAssignment_VersionStructure"
