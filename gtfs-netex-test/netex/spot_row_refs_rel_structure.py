from dataclasses import dataclass, field

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .spot_row_ref import SpotRowRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SpotRowRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "spotRowRefs_RelStructure"

    spot_row_ref: list[SpotRowRef] = field(
        default_factory=list,
        metadata={
            "name": "SpotRowRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
