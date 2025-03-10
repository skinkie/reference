from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .schematic_map import SchematicMap

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class SchematicMapsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "schematicMapsInFrame_RelStructure"

    schematic_map: list[SchematicMap] = field(
        default_factory=list,
        metadata={
            "name": "SchematicMap",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
