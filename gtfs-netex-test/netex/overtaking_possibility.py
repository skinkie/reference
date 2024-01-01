from dataclasses import dataclass, field
from .overtaking_possibility_version_structure import (
    OvertakingPossibilityVersionStructure,
)
from .point_ref_structure import PointRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OvertakingPossibility(OvertakingPossibilityVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    overtaking_at_point_ref: PointRefStructure = field(
        metadata={
            "name": "OvertakingAtPointRef",
            "type": "Element",
            "required": True,
        }
    )
