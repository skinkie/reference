from dataclasses import dataclass
from netex.path_junction_ref_structure import PathJunctionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PathJunctionRef(PathJunctionRefStructure):
    """
    Reference to a PATH JUNCTION.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
