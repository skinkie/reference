from dataclasses import dataclass, field
from typing import List
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.taxi_service_place_assignment import TaxiServicePlaceAssignment
from netex.vehicle_pooling_place_assignment import VehiclePoolingPlaceAssignment
from netex.vehicle_sharing_place_assignment import VehicleSharingPlaceAssignment

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleServicePlaceAssignmentsRelStructure(OneToManyRelationshipStructure):
    """Type for a list of VEHICLE SERVICE PLACE  ASSIGNMENTs.

    +v1.2.2
    """
    class Meta:
        name = "vehicleServicePlaceAssignments_RelStructure"

    vehicle_sharing_place_assignment_or_vehicle_pooling_place_assignment_or_taxi_service_place_assignment: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "VehicleSharingPlaceAssignment",
                    "type": VehicleSharingPlaceAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehiclePoolingPlaceAssignment",
                    "type": VehiclePoolingPlaceAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TaxiServicePlaceAssignment",
                    "type": TaxiServicePlaceAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
