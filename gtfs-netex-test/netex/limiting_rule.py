from dataclasses import dataclass, field
from netex.limiting_rule_versioned_structure import LimitingRuleVersionedStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class LimitingRule(LimitingRuleVersionedStructure):
    """
    A price for which a discount can be offered.

    :ivar id: Identifier of ENTITY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
