from dataclasses import dataclass
from netex.point_version_structure import PointVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class Point2(PointVersionStructure):
    """A 0-dimensional node of the network used for the spatial description of the
    network.

    POINTs may be located by a LOCATION in a given LOCATING SYSTEM.
    """
    class Meta:
        name = "Point"
        namespace = "http://www.netex.org.uk/netex"
