from dataclasses import dataclass, field
from typing import Optional

from .link_version_structure import LinkVersionStructure
from .path_instructions_rel_structure import PathInstructionsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GenericPathLinkVersionStructure(LinkVersionStructure):
    class Meta:
        name = "GenericPathLink_VersionStructure"

    path_instructions: Optional[PathInstructionsRelStructure] = field(
        default=None,
        metadata={
            "name": "pathInstructions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
