from dataclasses import dataclass

from .point_projection_structure import PointProjectionStructure

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass(kw_only=True)
class PointProjection(PointProjectionStructure):
    class Meta:
        namespace = "http://www.ifopt.org.uk/ifopt"
