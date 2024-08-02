from dataclasses import dataclass

from .estimated_service_journey_interchange_structure import EstimatedServiceJourneyInterchangeStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class EstimatedServiceJourneyInterchange(EstimatedServiceJourneyInterchangeStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
