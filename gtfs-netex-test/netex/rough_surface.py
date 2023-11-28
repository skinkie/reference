from dataclasses import dataclass, field
from netex.rough_surface_structure import RoughSurfaceStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RoughSurface(RoughSurfaceStructure):
    """
    Specialisation of PLACE EQUIPMENT for rough surfaces, giving properties of
    surface texture, mainly for impaired person information.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
