from dataclasses import dataclass, field
from decimal import Decimal
from typing import ForwardRef, List, Optional, Union

from .coordinates_structure import CoordinatesStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class LocationStructure:
    longitude_or_latitude_or_altitude_or_coordinates: List[Union["LocationStructure.Longitude", "LocationStructure.Latitude", "LocationStructure.Altitude", CoordinatesStructure]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "Longitude",
                    "type": ForwardRef("LocationStructure.Longitude"),
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "Latitude",
                    "type": ForwardRef("LocationStructure.Latitude"),
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "Altitude",
                    "type": ForwardRef("LocationStructure.Altitude"),
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "Coordinates",
                    "type": CoordinatesStructure,
                    "namespace": "http://www.siri.org.uk/siri",
                },
            ),
            "max_occurs": 3,
        },
    )
    precision: Optional[int] = field(
        default=None,
        metadata={
            "name": "Precision",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
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

    @dataclass(kw_only=True)
    class Longitude:
        value: Decimal = field(
            metadata={
                "required": True,
                "min_inclusive": Decimal("-180"),
                "max_inclusive": Decimal("180"),
            }
        )

    @dataclass(kw_only=True)
    class Latitude:
        value: Decimal = field(
            metadata={
                "required": True,
                "min_inclusive": Decimal("-90"),
                "max_inclusive": Decimal("90"),
            }
        )

    @dataclass(kw_only=True)
    class Altitude:
        value: Decimal = field(
            metadata={
                "required": True,
                "min_inclusive": Decimal("-1000"),
                "max_inclusive": Decimal("5000"),
            }
        )
