from dataclasses import dataclass

from .point_projection_ref_structure import PointProjectionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PointProjectionRef(PointProjectionRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
