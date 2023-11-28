from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from netex.pos import Pos

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class LocationStructure2:
    """Type for geospatial Position of a point.

    May be expressed in concrete WGS 84 Coordinates or any gml
    compatible point coordinates format.

    :ivar longitude: Longitude from Greenwich Meridian. -180 (East) to
        +180 (West). Decimal degrees. e.g. 2.356
    :ivar latitude: Latitude from equator. -90 (South) to +90 (North).
        Decimal degrees. e.g. 56.356
    :ivar altitude: Altitude (metres) Above sea level.
    :ivar pos:
    :ivar precision: Precision for point measurement. In meters.
    :ivar id: Identifier of point.
    :ivar srs_name: identifier of data Reference system for geocodes if
        point is specified as gml compatible Coordinates. A gml value.
        If not specified taken from system configuration.
    """
    class Meta:
        name = "LocationStructure"

    longitude: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Longitude",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_inclusive": Decimal("-180"),
            "max_inclusive": Decimal("180"),
        }
    )
    latitude: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Latitude",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_inclusive": Decimal("-90"),
            "max_inclusive": Decimal("90"),
        }
    )
    altitude: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Altitude",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_inclusive": Decimal("-1000"),
            "max_inclusive": Decimal("5000"),
        }
    )
    pos: Optional[Pos] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    precision: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Precision",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
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
