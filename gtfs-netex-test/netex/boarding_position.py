from dataclasses import dataclass, field
from netex.boarding_position_version_structure import BoardingPositionVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class BoardingPosition(BoardingPositionVersionStructure):
    """
    A location within a QUAY from which passengers may directly board, or onto
    which passengers may directly alight from, a VEHICLE.

    :ivar id: Identifier of BOARDING POSITION.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
