from dataclasses import dataclass
from netex.vehicle_service_place_assignment_ref_structure import VehicleServicePlaceAssignmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleServicePlaceAssignmentRef(VehicleServicePlaceAssignmentRefStructure):
    """Reference to a VEHICLE SERVICE PLACE ASSIGNMENT.

    +v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
