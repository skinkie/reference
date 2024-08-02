from dataclasses import dataclass

from .situation_exchange_capabilities_response_structure import SituationExchangeCapabilitiesResponseStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class SituationExchangeCapabilitiesResponse(SituationExchangeCapabilitiesResponseStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
