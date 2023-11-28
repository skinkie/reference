from dataclasses import dataclass
from netex.single_journey_path_ref_structure import SingleJourneyPathRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SingleJourneyPathRef(SingleJourneyPathRefStructure):
    """Reference to a SINGLE JOURNEY PATH.

    +v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
