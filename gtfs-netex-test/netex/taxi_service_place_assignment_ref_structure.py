from dataclasses import dataclass
from netex.vehicle_service_place_assignment_ref_structure import VehicleServicePlaceAssignmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TaxiServicePlaceAssignmentRefStructure(VehicleServicePlaceAssignmentRefStructure):
    """
    Type for a reference to a TAXI SERVICE PLACE ASSIGNMENT.
    """
