from dataclasses import dataclass
from netex.group_of_stop_places_ref_structure import GroupOfStopPlacesRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GroupOfStopPlacesRef(GroupOfStopPlacesRefStructure):
    """
    Reference to a GROUP OF STOP PLACEs.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
