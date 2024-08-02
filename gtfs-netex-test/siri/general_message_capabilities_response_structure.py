from dataclasses import dataclass, field
from typing import Optional

from .abstract_service_capabilities_response_structure import AbstractServiceCapabilitiesResponseStructure
from .extensions_1 import Extensions1
from .general_message_permissions import GeneralMessagePermissions
from .general_message_service_capabilities import GeneralMessageServiceCapabilities

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class GeneralMessageCapabilitiesResponseStructure(AbstractServiceCapabilitiesResponseStructure):
    general_message_service_capabilities: Optional[GeneralMessageServiceCapabilities] = field(
        default=None,
        metadata={
            "name": "GeneralMessageServiceCapabilities",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    general_message_permissions: Optional[GeneralMessagePermissions] = field(
        default=None,
        metadata={
            "name": "GeneralMessagePermissions",
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
