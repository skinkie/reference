from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .responsibility_set import ResponsibilitySet

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ResponsibilitySetsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "responsibilitySetsInFrame_RelStructure"

    responsibility_set: list[ResponsibilitySet] = field(
        default_factory=list,
        metadata={
            "name": "ResponsibilitySet",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
