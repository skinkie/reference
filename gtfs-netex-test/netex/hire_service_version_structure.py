from dataclasses import dataclass, field
from typing import List
from netex.hire_service_enumeration import HireServiceEnumeration
from netex.local_service_version_structure import LocalServiceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class HireServiceVersionStructure(LocalServiceVersionStructure):
    """
    Type for HIRE SERVICE.

    :ivar service_list: HIRE SERVICEs available.
    """
    class Meta:
        name = "HireService_VersionStructure"

    service_list: List[List[HireServiceEnumeration]] = field(
        default_factory=list,
        metadata={
            "name": "ServiceList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "tokens": True,
        }
    )
