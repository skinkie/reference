from dataclasses import dataclass

from .group_of_stop_places_ref_structure import GroupOfStopPlacesRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class GroupOfStopPlacesRef(GroupOfStopPlacesRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
