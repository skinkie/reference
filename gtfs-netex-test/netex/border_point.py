from dataclasses import dataclass, field
from netex.border_point_value_structure import BorderPointValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class BorderPoint(BorderPointValueStructure):
    """
    Designated BORDER POINT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
