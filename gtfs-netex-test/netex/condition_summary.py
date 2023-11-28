from dataclasses import dataclass
from netex.condition_summary_structure import ConditionSummaryStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ConditionSummary(ConditionSummaryStructure):
    """
    Summary description of PRODUCT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
