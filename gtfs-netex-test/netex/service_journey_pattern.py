from dataclasses import dataclass

from .service_journey_pattern_version_structure import ServiceJourneyPatternVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ServiceJourneyPattern(ServiceJourneyPatternVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
