from dataclasses import dataclass

from .group_of_places_ref_structure import GroupOfPlacesRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class GroupOfPlacesRef(GroupOfPlacesRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
