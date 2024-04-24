from dataclasses import dataclass, field
from typing import List

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .spot_column_ref import SpotColumnRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SpotColumnRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "spotColumnRefs_RelStructure"

    spot_column_ref: List[SpotColumnRef] = field(
        default_factory=list,
        metadata={
            "name": "SpotColumnRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
