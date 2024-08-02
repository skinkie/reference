from dataclasses import dataclass

from .connecting_journey_ref_structure import ConnectingJourneyRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class FeederRef(ConnectingJourneyRefStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
