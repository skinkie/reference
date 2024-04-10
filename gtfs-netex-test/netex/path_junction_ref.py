from dataclasses import dataclass

from .path_junction_ref_structure import PathJunctionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PathJunctionRef(PathJunctionRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
