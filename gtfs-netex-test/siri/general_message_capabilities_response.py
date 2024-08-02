from dataclasses import dataclass

from .general_message_capabilities_response_structure import GeneralMessageCapabilitiesResponseStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class GeneralMessageCapabilitiesResponse(GeneralMessageCapabilitiesResponseStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
