from dataclasses import dataclass, field
from netex.logical_display_version_structure import LogicalDisplayVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class LogicalDisplay(LogicalDisplayVersionStructure):
    """Represents a set of data that can be assembled for assignment to a physical
    PASSENGER INFORMATION EQUIPMENT or to a logical channel such as web or media.

    It is independent of any physical embodiment LOGICAL DISPLAY
    corresponds to a SIRI STOP MONITORING point.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
