from dataclasses import dataclass, field
from typing import List
from netex.abstract_curve_type import AbstractCurveType
from netex.point_property import PointProperty
from netex.pos import Pos
from netex.pos_list import PosList

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass(unsafe_hash=True, kw_only=True)
class LineStringType(AbstractCurveType):
    pos_or_point_property_or_pos_list: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "pos",
                    "type": Pos,
                    "namespace": "http://www.opengis.net/gml/3.2",
                },
                {
                    "name": "pointProperty",
                    "type": PointProperty,
                    "namespace": "http://www.opengis.net/gml/3.2",
                },
                {
                    "name": "posList",
                    "type": PosList,
                    "namespace": "http://www.opengis.net/gml/3.2",
                },
            ),
        }
    )
