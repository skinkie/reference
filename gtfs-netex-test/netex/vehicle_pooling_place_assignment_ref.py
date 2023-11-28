from dataclasses import dataclass
from netex.vehicle_pooling_place_assignment_ref_structure import VehiclePoolingPlaceAssignmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehiclePoolingPlaceAssignmentRef(VehiclePoolingPlaceAssignmentRefStructure):
    """Reference to a VEHICLE POOLING PLACE ASSIGNMENT.

    +v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
