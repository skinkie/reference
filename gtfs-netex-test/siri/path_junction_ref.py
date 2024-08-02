from dataclasses import dataclass

from .path_junction_ref_structure import PathJunctionRefStructure

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass(kw_only=True)
class PathJunctionRef(PathJunctionRefStructure):
    class Meta:
        namespace = "http://www.ifopt.org.uk/ifopt"
