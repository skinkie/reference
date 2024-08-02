from dataclasses import dataclass

from .situation_exchange_service_capabilities_structure import SituationExchangeServiceCapabilitiesStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class SituationExchangeServiceCapabilities(SituationExchangeServiceCapabilitiesStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
