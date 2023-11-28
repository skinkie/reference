from dataclasses import dataclass
from netex.customer_payment_means_ref_structure import CustomerPaymentMeansRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CustomerPaymentMeansRef(CustomerPaymentMeansRefStructure):
    """Reference to a CUSTOMER PAYMENT MEANS .

    +v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
