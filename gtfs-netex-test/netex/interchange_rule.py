from dataclasses import dataclass, field
from netex.interchange_rule_version_structure import InterchangeRuleVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class InterchangeRule(InterchangeRuleVersionStructure):
    """Conditions for considering journeys to meet or not to meet, specified
    indirectly: by a particular MODE, DIRECTION or LINE.

    Such conditions may alternatively be specified directly, indicating
    the corresponding services. In this case they are either a SERVICE
    JOURNEY PATTERN INTERCHANGE or a SERVICE JOURNEY INTERCHANGE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
