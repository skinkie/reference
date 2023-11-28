from dataclasses import dataclass, field
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.taxi_service_place_assignment_ref import TaxiServicePlaceAssignmentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TaxiServicePlaceAssignmentRefsRelStructure(OneToManyRelationshipStructure):
    """Type for a list of TAXI SERVICE PLACE ASSIGNMENTs.

    +v1.2.2
    """
    class Meta:
        name = "TaxiServicePlaceAssignmentRefs_RelStructure"

    taxi_service_place_assignment_ref: TaxiServicePlaceAssignmentRef = field(
        metadata={
            "name": "TaxiServicePlaceAssignmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
