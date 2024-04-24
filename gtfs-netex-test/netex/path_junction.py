from dataclasses import dataclass, field
from typing import Any

from .site_path_junction_version_structure import SitePathJunctionVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PathJunction(SitePathJunctionVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    path_instructions: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
