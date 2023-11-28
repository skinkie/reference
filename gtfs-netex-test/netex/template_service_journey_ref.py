from dataclasses import dataclass
from netex.template_service_journey_ref_structure import TemplateServiceJourneyRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TemplateServiceJourneyRef(TemplateServiceJourneyRefStructure):
    """
    Reference to a TEMPLATE VEHICLE JOURNEY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
