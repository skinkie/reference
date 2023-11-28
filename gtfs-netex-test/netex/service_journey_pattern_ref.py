from dataclasses import dataclass
from netex.service_journey_pattern_ref_structure import ServiceJourneyPatternRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ServiceJourneyPatternRef(ServiceJourneyPatternRefStructure):
    """
    Reference to a SERVICE JOURNEY PATTERN.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
