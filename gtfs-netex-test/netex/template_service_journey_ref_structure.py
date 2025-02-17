from dataclasses import dataclass

from .service_journey_ref_structure import ServiceJourneyRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TemplateServiceJourneyRefStructure(ServiceJourneyRefStructure):
    pass
