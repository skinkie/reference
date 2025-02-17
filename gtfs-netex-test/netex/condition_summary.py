from dataclasses import dataclass

from .condition_summary_structure import ConditionSummaryStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ConditionSummary(ConditionSummaryStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
