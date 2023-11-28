from dataclasses import dataclass
from netex.customer_service_version_structure import CustomerServiceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CustomerService(CustomerServiceVersionStructure):
    """
    Generic specialisation of LOCAL SERVICE for CUSTOMER SERVICEs (lost properties,
    meeting point, complaints, etc.).
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
