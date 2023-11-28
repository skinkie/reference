from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.offered_travel_specification import OfferedTravelSpecification
from netex.offered_travel_specification_ref import OfferedTravelSpecificationRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class OfferedTravelSpecificationsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of TRAVEL SPECIFICATIONs.
    """
    class Meta:
        name = "offeredTravelSpecifications_RelStructure"

    offered_travel_specification_ref_or_offered_travel_specification: List[object] = field(
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
                    "name": "OfferedTravelSpecification",
                    "type": OfferedTravelSpecification,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
