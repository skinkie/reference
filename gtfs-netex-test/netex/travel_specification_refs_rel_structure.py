from dataclasses import dataclass, field
from typing import List
from netex.offered_travel_specification_ref import OfferedTravelSpecificationRef
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.requested_travel_specification_ref import RequestedTravelSpecificationRef
from netex.travel_specification_ref import TravelSpecificationRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TravelSpecificationRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a collection of one or more references to a TRAVEL SPECIFICATION.
    """
    class Meta:
        name = "travelSpecificationRefs_RelStructure"

    offered_travel_specification_ref_or_requested_travel_specification_ref_or_travel_specification_ref: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "OfferedTravelSpecificationRef",
                    "type": OfferedTravelSpecificationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RequestedTravelSpecificationRef",
                    "type": RequestedTravelSpecificationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TravelSpecificationRef",
                    "type": TravelSpecificationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
