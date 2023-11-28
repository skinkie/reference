from dataclasses import dataclass
from netex.service_journey_ref_structure import ServiceJourneyRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TemplateServiceJourneyRefStructure(ServiceJourneyRefStructure):
    """
    Type for a reference to a TEMPLATE VEHICLE JOURNEY.
    """
