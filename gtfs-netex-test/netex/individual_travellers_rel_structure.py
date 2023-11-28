from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.individual_traveller import IndividualTraveller
from netex.individual_traveller_ref import IndividualTravellerRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class IndividualTravellersRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of INDIVIDUAL TRAVELLERs.
    """
    class Meta:
        name = "individualTravellers_RelStructure"

    individual_traveller_ref_or_individual_traveller: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "IndividualTravellerRef",
                    "type": IndividualTravellerRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "IndividualTraveller",
                    "type": IndividualTraveller,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
