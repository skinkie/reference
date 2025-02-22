from dataclasses import dataclass, field
from typing import Optional

from .type_of_place_refs_rel_structure import TypeOfPlaceRefsRelStructure
from .zone_version_structure import ZoneVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class PlaceVersionStructure(ZoneVersionStructure):
    class Meta:
        name = "Place_VersionStructure"

    place_types: Optional[TypeOfPlaceRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "placeTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
