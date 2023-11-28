from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.customer_payment_means import CustomerPaymentMeans

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CustomerPaymentMeansRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of a CUSTOMER PAYMENT MEANSs in Sequence.

    :ivar customer_payment_means: A component (mobile phone, smart card,
        etc) with the necessary facilities (hardware and software) to
        host a CUSTOMER PAYMENT MEANS and communicate with a control
        device. +v1.2.2
    """
    class Meta:
        name = "customerPaymentMeans_RelStructure"

    customer_payment_means: List[CustomerPaymentMeans] = field(
        default_factory=list,
        metadata={
            "name": "CustomerPaymentMeans",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
