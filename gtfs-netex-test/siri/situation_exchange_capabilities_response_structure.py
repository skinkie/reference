from dataclasses import dataclass, field
from typing import Optional

from .abstract_service_capabilities_response_structure import AbstractServiceCapabilitiesResponseStructure
from .extensions_1 import Extensions1
from .situation_exchange_permissions import SituationExchangePermissions
from .situation_exchange_service_capabilities import SituationExchangeServiceCapabilities

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class SituationExchangeCapabilitiesResponseStructure(AbstractServiceCapabilitiesResponseStructure):
    situation_exchange_service_capabilities: Optional[SituationExchangeServiceCapabilities] = field(
        default=None,
        metadata={
            "name": "SituationExchangeServiceCapabilities",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    situation_exchange_permissions: Optional[SituationExchangePermissions] = field(
        default=None,
        metadata={
            "name": "SituationExchangePermissions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    extensions: Optional[Extensions1] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    version: str = field(
        default="2.1",
        metadata={
            "type": "Attribute",
        },
    )
