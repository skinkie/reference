from dataclasses import dataclass
from netex.interchange_rule_timing_ref_structure import InterchangeRuleTimingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class InterchangeRuleTimingRef(InterchangeRuleTimingRefStructure):
    """
    Reference to an INTERCHANGE RULE TIMING.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
