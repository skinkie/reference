from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from .abstract_projection import AbstractProjection
from .coordinates_structure import CoordinatesStructure

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass(kw_only=True)
class PointProjectionStructure(AbstractProjection):
    longitude: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Longitude",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
            "min_inclusive": Decimal("-180"),
            "max_inclusive": Decimal("180"),
        },
    )
    latitude: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Latitude",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
            "min_inclusive": Decimal("-90"),
            "max_inclusive": Decimal("90"),
        },
    )
    altitude: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Altitude",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
            "min_inclusive": Decimal("-1000"),
            "max_inclusive": Decimal("5000"),
        },
    )
    coordinates: Optional[CoordinatesStructure] = field(
        default=None,
        metadata={
            "name": "Coordinates",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        },
    )
    precision: Optional[int] = field(
        default=None,
        metadata={
            "name": "Precision",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    srs_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "srsName",
            "type": "Attribute",
        },
    )
