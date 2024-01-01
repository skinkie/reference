from dataclasses import dataclass
from .path_junction_ref_structure import PathJunctionRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PathJunctionRef(PathJunctionRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
