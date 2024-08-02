from dataclasses import dataclass

from .general_message_service_capabilities_structure import GeneralMessageServiceCapabilitiesStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class GeneralMessageServiceCapabilities(GeneralMessageServiceCapabilitiesStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
