from dataclasses import dataclass

from .service_journey_pattern_interchange_version_structure import ServiceJourneyPatternInterchangeVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ServiceJourneyPatternInterchange(ServiceJourneyPatternInterchangeVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
