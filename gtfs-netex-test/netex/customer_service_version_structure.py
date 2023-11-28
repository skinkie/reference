from dataclasses import dataclass
from netex.local_service_version_structure import LocalServiceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CustomerServiceVersionStructure(LocalServiceVersionStructure):
    """
    Type for CUSTOMER SERVICE.
    """
    class Meta:
        name = "CustomerService_VersionStructure"
