from dataclasses import dataclass, field

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .type_of_zone_ref import TypeOfZoneRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TypeOfZoneRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "typeOfZoneRefs_RelStructure"

    type_of_zone_ref: list[TypeOfZoneRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
