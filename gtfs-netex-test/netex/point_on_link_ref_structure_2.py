from dataclasses import dataclass, field
from typing import Optional
from .point_ref_structure import PointRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PointOnLinkRefStructure2(PointRefStructure):
    class Meta:
        name = "PointOnLinkRefStructure_"

    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
