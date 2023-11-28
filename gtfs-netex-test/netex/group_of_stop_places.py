from dataclasses import dataclass, field
from netex.group_of_stop_places_structure import GroupOfStopPlacesStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GroupOfStopPlaces(GroupOfStopPlacesStructure):
    """
    Group of STOP PLACEs.

    :ivar id: Identifier of GROUP of STOP PLACEs.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
