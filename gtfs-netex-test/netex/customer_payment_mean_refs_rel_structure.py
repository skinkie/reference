from dataclasses import dataclass, field
from typing import List
from netex.customer_payment_means_ref import CustomerPaymentMeansRef
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CustomerPaymentMeanRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of CUSTOMER PAYMENT MEANS.
    """
    class Meta:
        name = "customerPaymentMeanRefs_RelStructure"

    customer_payment_means_ref: List[CustomerPaymentMeansRef] = field(
        default_factory=list,
        metadata={
            "name": "CustomerPaymentMeansRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
