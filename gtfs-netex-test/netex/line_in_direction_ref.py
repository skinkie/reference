from dataclasses import dataclass
from netex.line_in_direction_ref_structure import LineInDirectionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class LineInDirectionRef(LineInDirectionRefStructure):
    """
    Refrence to LINE in a specific DIRECTION.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
