from dataclasses import dataclass
from .group_of_places_version_structure import GroupOfPlacesVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupOfPlaces(GroupOfPlacesVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
