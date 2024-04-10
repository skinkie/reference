from dataclasses import dataclass

from .service_journey_interchange_ref_structure import ServiceJourneyInterchangeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServiceJourneyInterchangeRef(ServiceJourneyInterchangeRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
