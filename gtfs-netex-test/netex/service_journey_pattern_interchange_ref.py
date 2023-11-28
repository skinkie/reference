from dataclasses import dataclass
from netex.service_journey_pattern_interchange_ref_structure import ServiceJourneyPatternInterchangeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ServiceJourneyPatternInterchangeRef(ServiceJourneyPatternInterchangeRefStructure):
    """
    Reference to a SERVICE JOURNEY PATTERN INTERCHANGE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
