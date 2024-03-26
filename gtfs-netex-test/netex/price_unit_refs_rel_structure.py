from dataclasses import dataclass, field
from typing import List

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .price_unit_ref import PriceUnitRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PriceUnitRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "priceUnitRefs_RelStructure"

    price_unit_ref: List[PriceUnitRef] = field(
        default_factory=list,
        metadata={
            "name": "PriceUnitRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
