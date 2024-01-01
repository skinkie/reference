from dataclasses import dataclass
from .customer_service_version_structure import CustomerServiceVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ComplaintsServiceVersionStructure(CustomerServiceVersionStructure):
    class Meta:
        name = "ComplaintsService_VersionStructure"
