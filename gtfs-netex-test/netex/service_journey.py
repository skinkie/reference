from dataclasses import dataclass

from .service_journey_version_structure import ServiceJourneyVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ServiceJourney(ServiceJourneyVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
