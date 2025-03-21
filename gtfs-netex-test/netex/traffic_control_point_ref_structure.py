from dataclasses import dataclass

from .point_ref_structure import PointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TrafficControlPointRefStructure(PointRefStructure):
    pass
