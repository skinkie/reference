from dataclasses import dataclass, field
from typing import List
from .communication_service_enumeration import CommunicationServiceEnumeration
from .local_service_version_structure import LocalServiceVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CommunicationServiceVersionStructure(LocalServiceVersionStructure):
    class Meta:
        name = "CommunicationService_VersionStructure"

    service_list: List[CommunicationServiceEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "ServiceList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
            "tokens": True,
        },
    )
