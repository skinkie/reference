from dataclasses import dataclass
from .rough_surface_structure import RoughSurfaceStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RoughSurface(RoughSurfaceStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
