from dataclasses import dataclass, field
from typing import Optional
from netex.type_of_place_refs_rel_structure import TypeOfPlaceRefsRelStructure
from netex.zone_version_structure import ZoneVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PlaceVersionStructure(ZoneVersionStructure):
    """
    Type for a PLACE.

    :ivar place_types: Classification of PLACE.
    """
    class Meta:
        name = "Place_VersionStructure"

    place_types: Optional[TypeOfPlaceRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "placeTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
