from dataclasses import dataclass
from netex.customer_account_status_ref_structure import CustomerAccountStatusRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CustomerAccountStatusRef(CustomerAccountStatusRefStructure):
    """
    Reference to a CUSTOMER ACCOUNT STATUS .
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
