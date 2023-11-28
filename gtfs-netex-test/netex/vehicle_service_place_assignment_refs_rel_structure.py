from dataclasses import dataclass, field
from typing import Optional
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.taxi_service_place_assignment_ref import TaxiServicePlaceAssignmentRef
from netex.vehicle_pooling_place_assignment_ref import VehiclePoolingPlaceAssignmentRef
from netex.vehicle_service_place_assignment_ref import VehicleServicePlaceAssignmentRef
from netex.vehicle_sharing_place_assignment_ref import VehicleSharingPlaceAssignmentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleServicePlaceAssignmentRefsRelStructure(OneToManyRelationshipStructure):
    """Type for a list of VEHICLE SERVICE PLACE ASSIGNMENTs.

    +v1.2.2
    """
    class Meta:
        name = "vehicleServicePlaceAssignmentRefs_RelStructure"

    choice: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "VehiclePoolingPlaceAssignmentRef",
                    "type": VehiclePoolingPlaceAssignmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleSharingPlaceAssignmentRef",
                    "type": VehicleSharingPlaceAssignmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TaxiServicePlaceAssignmentRef",
                    "type": TaxiServicePlaceAssignmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleServicePlaceAssignmentRef",
                    "type": VehicleServicePlaceAssignmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
