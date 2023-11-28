from dataclasses import dataclass
from netex.boarding_position_ref_structure import BoardingPositionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class BoardingPositionRef(BoardingPositionRefStructure):
    """
    Reference to a BOARDING POSITION.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
