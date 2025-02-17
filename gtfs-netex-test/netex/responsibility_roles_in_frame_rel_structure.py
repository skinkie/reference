from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .responsibility_role import ResponsibilityRole

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ResponsibilityRolesInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "responsibilityRolesInFrame_RelStructure"

    responsibility_role: list[ResponsibilityRole] = field(
        default_factory=list,
        metadata={
            "name": "ResponsibilityRole",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
