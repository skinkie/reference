from dataclasses import dataclass

from .local_service_version_structure import LocalServiceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class CustomerServiceVersionStructure(LocalServiceVersionStructure):
    class Meta:
        name = "CustomerService_VersionStructure"
