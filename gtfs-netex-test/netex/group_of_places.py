from dataclasses import dataclass, field
from netex.group_of_places_version_structure import GroupOfPlacesVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GroupOfPlaces(GroupOfPlacesVersionStructure):
    """
    A grouping of PLACEs which will be commonly referenced for a specific purpose.

    :ivar id: Identifier of  GROUP OF PLACES.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
