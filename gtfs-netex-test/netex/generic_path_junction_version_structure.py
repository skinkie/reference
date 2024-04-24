from dataclasses import dataclass, field
from typing import Optional

from .path_instructions_rel_structure import PathInstructionsRelStructure
from .point_version_structure import PointVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GenericPathJunctionVersionStructure(PointVersionStructure):
    class Meta:
        name = "GenericPathJunction_VersionStructure"

    path_instructions: Optional[PathInstructionsRelStructure] = field(
        default=None,
        metadata={
            "name": "pathInstructions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
