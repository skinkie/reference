from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class StairEndStructure:
    """
    End of Flight of stairs.

    :ivar continuing_handrail: Whether there is a handrail that
        continues from previous section.
    :ivar textured_surface: Whether there is a textured ground surface.
    :ivar visual_contrast: Whether there is a colour contrast.
    """
    continuing_handrail: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ContinuingHandrail",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    textured_surface: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TexturedSurface",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    visual_contrast: Optional[bool] = field(
        default=None,
        metadata={
            "name": "VisualContrast",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
