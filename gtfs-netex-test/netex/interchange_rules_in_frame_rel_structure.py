from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .interchange_rule import InterchangeRule

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class InterchangeRulesInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "interchangeRulesInFrame_RelStructure"

    interchange_rule: list[InterchangeRule] = field(
        default_factory=list,
        metadata={
            "name": "InterchangeRule",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
