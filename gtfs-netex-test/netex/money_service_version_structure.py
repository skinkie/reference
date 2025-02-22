from dataclasses import dataclass, field

from .local_service_version_structure import LocalServiceVersionStructure
from .money_service_enumeration import MoneyServiceEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class MoneyServiceVersionStructure(LocalServiceVersionStructure):
    class Meta:
        name = "MoneyService_VersionStructure"

    service_list: list[MoneyServiceEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "ServiceList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
