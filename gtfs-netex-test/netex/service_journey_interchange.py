from dataclasses import dataclass

from .service_journey_interchange_version_structure import ServiceJourneyInterchangeVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ServiceJourneyInterchange(ServiceJourneyInterchangeVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
