from dataclasses import dataclass
from netex.customer_service_ref_structure import CustomerServiceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CustomerServiceRef(CustomerServiceRefStructure):
    """
    Identifier of an CUSTOMER SERVICE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
