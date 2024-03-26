from dataclasses import dataclass, field
from typing import List

from .flexible_line_ref import FlexibleLineRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FlexibleLineRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "flexibleLineRefs_RelStructure"

    flexible_line_ref: List[FlexibleLineRef] = field(
        default_factory=list,
        metadata={
            "name": "FlexibleLineRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
