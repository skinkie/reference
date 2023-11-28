from dataclasses import dataclass, field
from netex.customer_payment_means_versioned_child_structure import CustomerPaymentMeansVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CustomerPaymentMeans(CustomerPaymentMeansVersionedChildStructure):
    """
    A registered means with which a TRANSPORT CUSTOMER wishes to make payments for
    a CUSTOMER ACCOUNT, e.g. by nominated EMV card,

    :ivar id: Identifier of ENTITY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
