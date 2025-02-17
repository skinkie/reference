from dataclasses import dataclass

from .relationship_structure import RelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class StrictContainmentAggregationStructure(RelationshipStructure):
    class Meta:
        name = "strictContainmentAggregationStructure"
