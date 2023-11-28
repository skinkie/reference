from dataclasses import dataclass, field
from typing import Optional
from netex.address_version_structure import AddressVersionStructure
from netex.compass_bearing16_enumeration import CompassBearing16Enumeration
from netex.multilingual_string import MultilingualString
from netex.road_number_range_structure import RoadNumberRangeStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RoadAddressVersionStructure(AddressVersionStructure):
    """
    Type for Road ADDRESS.

    :ivar gis_feature_ref: Reference to a GIS feature identifier.
    :ivar road_number: Road Number.
    :ivar road_name: Road name.
    :ivar bearing_compass: Bearing of Road at point in compass octants
        to North.
    :ivar bearing_degrees: Bearing of Road in absolute degrees against
        North.
    :ivar odd_number_range: Range of odd house numbers that the ROAD
        ADDRESS covers.
    :ivar even_number_range: Range of even house numbers that the ROAD
        ADDRESS covers.
    """
    class Meta:
        name = "RoadAddress_VersionStructure"

    gis_feature_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "GisFeatureRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    road_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "RoadNumber",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    road_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "RoadName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    bearing_compass: Optional[CompassBearing16Enumeration] = field(
        default=None,
        metadata={
            "name": "BearingCompass",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    bearing_degrees: Optional[int] = field(
        default=None,
        metadata={
            "name": "BearingDegrees",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    odd_number_range: Optional[RoadNumberRangeStructure] = field(
        default=None,
        metadata={
            "name": "OddNumberRange",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    even_number_range: Optional[RoadNumberRangeStructure] = field(
        default=None,
        metadata={
            "name": "EvenNumberRange",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
