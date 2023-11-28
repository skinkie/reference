from dataclasses import dataclass, field
from netex.accessibility_limitation import AccessibilityLimitation
from netex.strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AccessibilityLimitationsRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of ACCESSIBILITY LIMITATIONs.

    :ivar accessibility_limitation: Assessment of the accessibility of a
        SITE.
    """
    class Meta:
        name = "accessibilityLimitations_RelStructure"

    accessibility_limitation: AccessibilityLimitation = field(
        metadata={
            "name": "AccessibilityLimitation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
