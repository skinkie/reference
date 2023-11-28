from dataclasses import dataclass, field
from netex.capping_rule_versioned_child_structure import CappingRuleVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CappingRule(CappingRuleVersionedChildStructure):
    """
    Rule about capping for a mode.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
