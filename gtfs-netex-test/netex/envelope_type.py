from dataclasses import dataclass, field
from typing import List, Optional
from netex.direct_position_type import DirectPositionType
from netex.pos import Pos

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass(unsafe_hash=True, kw_only=True)
class EnvelopeType:
    lower_corner_or_upper_corner_or_pos: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "lowerCorner",
                    "type": DirectPositionType,
                    "namespace": "http://www.opengis.net/gml/3.2",
                },
                {
                    "name": "upperCorner",
                    "type": DirectPositionType,
                    "namespace": "http://www.opengis.net/gml/3.2",
                },
                {
                    "name": "pos",
                    "type": Pos,
                    "namespace": "http://www.opengis.net/gml/3.2",
                },
            ),
            "max_occurs": 2,
        }
    )
    srs_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "srsName",
            "type": "Attribute",
        }
    )
    srs_dimension: Optional[int] = field(
        default=None,
        metadata={
            "name": "srsDimension",
            "type": "Attribute",
        }
    )
