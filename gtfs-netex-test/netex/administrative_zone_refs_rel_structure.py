from dataclasses import dataclass, field

from .administrative_zone_ref import AdministrativeZoneRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class AdministrativeZoneRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "administrativeZoneRefs_RelStructure"

    administrative_zone_ref: list[AdministrativeZoneRef] = field(
        default_factory=list,
        metadata={
            "name": "AdministrativeZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
