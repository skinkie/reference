from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .entity_in_version_structure import ValidityRuleParameterVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ValidityRuleParametersRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "validityRuleParameters_RelStructure"

    validity_rule_parameter: list[ValidityRuleParameterVersionStructure] = field(
        default_factory=list,
        metadata={
            "name": "ValidityRuleParameter",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
