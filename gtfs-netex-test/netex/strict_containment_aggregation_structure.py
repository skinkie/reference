from dataclasses import dataclass
from .relationship_structure import RelationshipStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class StrictContainmentAggregationStructure(RelationshipStructure):
    class Meta:
        name = "strictContainmentAggregationStructure"
