from dataclasses import dataclass, field
from netex.place_lighting_version_structure import PlaceLightingVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PlaceLighting(PlaceLightingVersionStructure):
    """
    Specialisation of PLACE EQUIPMENT for LIGHTING EQUIPMENT (e.g. lamp post).
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
