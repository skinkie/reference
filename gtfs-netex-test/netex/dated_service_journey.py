from dataclasses import dataclass

from .dated_service_journey_version_structure import DatedServiceJourneyVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class DatedServiceJourney(DatedServiceJourneyVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
