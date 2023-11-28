from dataclasses import dataclass, field
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.vehicle_pooling_place_assignment_ref import VehiclePoolingPlaceAssignmentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehiclePoolingPlaceAssignmentRefsRelStructure(OneToManyRelationshipStructure):
    """Type for a list of VEHICLE POOLING PLACE ASSIGNMENTs.

    +v1.2.2
    """
    class Meta:
        name = "VehiclePoolingPlaceAssignmentRefs_RelStructure"

    vehicle_pooling_place_assignment_ref: VehiclePoolingPlaceAssignmentRef = field(
        metadata={
            "name": "VehiclePoolingPlaceAssignmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
