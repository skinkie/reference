from dataclasses import dataclass
from netex.connecting_journey_derived_view_structure import ConnectingJourneyDerivedViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ConnectingJourneyView(ConnectingJourneyDerivedViewStructure):
    """
    Simplified  view of CONNECTING JOURNEY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
