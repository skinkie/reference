from dataclasses import dataclass, field
from typing import Optional


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RelationshipStructure:
    class Meta:
        name = "relationshipStructure"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
