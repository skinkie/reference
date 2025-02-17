from dataclasses import dataclass, field

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .place_ref import PlaceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class PlaceRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "placeRefs_RelStructure"

    place_ref: list[PlaceRef] = field(
        default_factory=list,
        metadata={
            "name": "PlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
