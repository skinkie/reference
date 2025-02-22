from dataclasses import dataclass

from .connecting_journey_derived_view_structure import ConnectingJourneyDerivedViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ConnectingJourneyView(ConnectingJourneyDerivedViewStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
