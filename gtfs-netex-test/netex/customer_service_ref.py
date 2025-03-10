from dataclasses import dataclass

from .customer_service_ref_structure import CustomerServiceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class CustomerServiceRef(CustomerServiceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
