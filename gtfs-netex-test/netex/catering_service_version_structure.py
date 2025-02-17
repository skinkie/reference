from dataclasses import dataclass, field

from .catering_service_enumeration import CateringServiceEnumeration
from .local_service_version_structure import LocalServiceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class CateringServiceVersionStructure(LocalServiceVersionStructure):
    class Meta:
        name = "CateringService_VersionStructure"

    service_list: list[CateringServiceEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "ServiceList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
