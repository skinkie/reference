from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.retail_consortium import RetailConsortium
from netex.retail_consortium_ref import RetailConsortiumRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RetailConsortiumsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of RETAIL CONSORTIUMs.
    """
    class Meta:
        name = "retailConsortiums_RelStructure"

    retail_consortium_ref_or_retail_consortium: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "RetailConsortiumRef",
                    "type": RetailConsortiumRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RetailConsortium",
                    "type": RetailConsortium,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
