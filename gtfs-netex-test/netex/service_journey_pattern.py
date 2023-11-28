from dataclasses import dataclass, field
from netex.service_journey_pattern_version_structure import ServiceJourneyPatternVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ServiceJourneyPattern(ServiceJourneyPatternVersionStructure):
    """
    The JOURNEY PATTERN for a (passenger carrying) SERVICE JOURNEY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
