from dataclasses import dataclass
from netex.default_service_journey_time_ref_structure import DefaultServiceJourneyTimeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DefaultServiceJourneyTimeRef(DefaultServiceJourneyTimeRefStructure):
    """
    Reference to a DEFAULT SERVICE JOURNEY TIME.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
