from dataclasses import dataclass, field
from typing import Any

from .capping_rule_versioned_child_structure import CappingRuleVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CappingRule(CappingRuleVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    private_codes: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
