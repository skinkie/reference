from dataclasses import dataclass, field
from netex.template_service_journey_version_structure import TemplateServiceJourneyVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TemplateServiceJourney(TemplateServiceJourneyVersionStructure):
    """
    A VEHICLE JOURNEY with a set of frequencies that may be used to represent a set
    of similar journeys differing only by their time of departure.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
