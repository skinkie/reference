from dataclasses import dataclass
from netex.single_journey_ref_structure import SingleJourneyRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SingleJourneyRef(SingleJourneyRefStructure):
    """Reference to a SINGLE JOURNEY.

    +v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
