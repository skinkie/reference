from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(unsafe_hash=True, kw_only=True)
class LocationStructure1:
    """Type for gepspatial Position of a point.

    May be expressed in concrete WGS 84 Coordinates or any gml
    compatible point coordinates format.

    :ivar longitude_or_latitude_or_coordinates:
    :ivar precision: Precision for point measurement. In meters.
    :ivar id: Identifier of POINT.
    :ivar srs_name: identifier of data reference system for geocodes if
        point is specified as gml compatible Coordinates. A gml value.
        If not specified taken from system configuration.
    """
    class Meta:
        name = "LocationStructure"

    longitude_or_latitude_or_coordinates: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "Longitude",
                    "type": Decimal,
                    "namespace": "http://www.siri.org.uk/siri",
                    "min_inclusive": Decimal("-180"),
                    "max_inclusive": Decimal("180"),
                },
                {
                    "name": "Latitude",
                    "type": Decimal,
                    "namespace": "http://www.siri.org.uk/siri",
                    "min_inclusive": Decimal("-90"),
                    "max_inclusive": Decimal("90"),
                },
                {
                    "name": "Coordinates",
                    "type": List[str],
                    "namespace": "http://www.siri.org.uk/siri",
                    "default_factory": list,
                    "tokens": True,
                },
            ),
            "max_occurs": 2,
        }
    )
    precision: Optional[int] = field(
        default=None,
        metadata={
            "name": "Precision",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    srs_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "srsName",
            "type": "Attribute",
        }
    )
