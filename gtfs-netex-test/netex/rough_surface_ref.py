from dataclasses import dataclass
from netex.rough_surface_ref_structure import RoughSurfaceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RoughSurfaceRef(RoughSurfaceRefStructure):
    """
    Identifier of an ROUGH SURFACE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
