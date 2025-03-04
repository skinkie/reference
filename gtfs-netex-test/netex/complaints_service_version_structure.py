from dataclasses import dataclass

from .customer_service_version_structure import CustomerServiceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ComplaintsServiceVersionStructure(CustomerServiceVersionStructure):
    class Meta:
        name = "ComplaintsService_VersionStructure"
