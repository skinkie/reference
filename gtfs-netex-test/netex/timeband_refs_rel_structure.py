from dataclasses import dataclass, field

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .timeband_ref import TimebandRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TimebandRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "timebandRefs_RelStructure"

    timeband_ref: list[TimebandRef] = field(
        default_factory=list,
        metadata={
            "name": "TimebandRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
