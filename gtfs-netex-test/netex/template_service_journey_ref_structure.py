from dataclasses import dataclass
from .service_journey_ref_structure import ServiceJourneyRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TemplateServiceJourneyRefStructure(ServiceJourneyRefStructure):
    value: RestrictedVar
