from dataclasses import dataclass
from netex.vehicle_service_place_assignment_ref_structure import VehicleServicePlaceAssignmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleSharingPlaceAssignmentRefStructure(VehicleServicePlaceAssignmentRefStructure):
    """
    Type for a reference to a VEHICLE SHARING PLACE ASSIGNMENT.
    """
