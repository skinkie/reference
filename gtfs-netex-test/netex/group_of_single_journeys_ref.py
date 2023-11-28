from dataclasses import dataclass
from netex.group_of_single_journeys_ref_structure import GroupOfSingleJourneysRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GroupOfSingleJourneysRef(GroupOfSingleJourneysRefStructure):
    """Reference to a GROUP OF SINGLE JOURNEYs.

    +v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
