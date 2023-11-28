from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.customer import Customer
from netex.customer_ref import CustomerRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CustomersRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of CUSTOMERs.
    """
    class Meta:
        name = "customers_RelStructure"

    customer_ref_or_customer: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "CustomerRef",
                    "type": CustomerRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Customer",
                    "type": Customer,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
