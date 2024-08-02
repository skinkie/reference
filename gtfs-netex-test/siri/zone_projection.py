from dataclasses import dataclass

from .zone_projection_structure import ZoneProjectionStructure

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass(kw_only=True)
class ZoneProjection(ZoneProjectionStructure):
    class Meta:
        namespace = "http://www.ifopt.org.uk/ifopt"
