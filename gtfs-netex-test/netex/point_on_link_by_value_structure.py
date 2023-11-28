from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PointOnLinkByValueStructure:
    """
    Type for a  reference to POINT ON LINK by Distance.

    :ivar distance_from_start: Distance of Point on Link from start of
        LINK.
    """
    distance_from_start: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DistanceFromStart",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
