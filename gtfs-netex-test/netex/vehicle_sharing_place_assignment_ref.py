from dataclasses import dataclass
from netex.vehicle_sharing_place_assignment_ref_structure import VehicleSharingPlaceAssignmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleSharingPlaceAssignmentRef(VehicleSharingPlaceAssignmentRefStructure):
    """Reference to a VEHICLE SHARING PLACE ASSIGNMENT.

    +v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
