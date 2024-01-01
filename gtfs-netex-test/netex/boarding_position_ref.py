from dataclasses import dataclass
from .boarding_position_ref_structure import BoardingPositionRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class BoardingPositionRef(BoardingPositionRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
