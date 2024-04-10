from dataclasses import dataclass

from .customer_service_version_structure import CustomerServiceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CustomerService(CustomerServiceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
