from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .customer_payment_means import CustomerPaymentMeans

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class CustomerPaymentMeansRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "customerPaymentMeans_RelStructure"

    customer_payment_means: list[CustomerPaymentMeans] = field(
        default_factory=list,
        metadata={
            "name": "CustomerPaymentMeans",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
