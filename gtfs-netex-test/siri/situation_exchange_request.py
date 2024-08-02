from dataclasses import dataclass

from .situation_exchange_request_structure import SituationExchangeRequestStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class SituationExchangeRequest(SituationExchangeRequestStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
