from dataclasses import dataclass, field
from typing import List, Optional, Union

from .abstract_referencing_item_structure import AbstractReferencingItemStructure
from .branding_ref_structure import BrandingRefStructure
from .branding_structure import BrandingStructure
from .direction_ref_structure import DirectionRefStructure
from .extensions_1 import Extensions1
from .framed_vehicle_journey_ref_structure import FramedVehicleJourneyRefStructure
from .group_of_lines_ref_structure import GroupOfLinesRefStructure
from .journey_pattern_ref_structure import JourneyPatternRefStructure
from .line_ref_structure import LineRefStructure
from .natural_language_string_structure import NaturalLanguageStringStructure
from .published_line_name import PublishedLineName
from .route_ref_structure import RouteRefStructure
from .vehicle_modes_enumeration import VehicleModesEnumeration
from .vehicle_monitoring_ref_structure import VehicleMonitoringRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class VehicleActivityCancellationStructure(AbstractReferencingItemStructure):
    vehicle_monitoring_ref: Optional[VehicleMonitoringRefStructure] = field(
        default=None,
        metadata={
            "name": "VehicleMonitoringRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    vehicle_journey_ref: Optional[FramedVehicleJourneyRefStructure] = field(
        default=None,
        metadata={
            "name": "VehicleJourneyRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    line_ref: Optional[LineRefStructure] = field(
        default=None,
        metadata={
            "name": "LineRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    direction_ref: Optional[DirectionRefStructure] = field(
        default=None,
        metadata={
            "name": "DirectionRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    journey_pattern_ref: Optional[JourneyPatternRefStructure] = field(
        default=None,
        metadata={
            "name": "JourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    journey_pattern_name: Optional[NaturalLanguageStringStructure] = field(
        default=None,
        metadata={
            "name": "JourneyPatternName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    vehicle_mode: List[VehicleModesEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "VehicleMode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    route_ref: Optional[RouteRefStructure] = field(
        default=None,
        metadata={
            "name": "RouteRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    published_line_name: List[PublishedLineName] = field(
        default_factory=list,
        metadata={
            "name": "PublishedLineName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    group_of_lines_ref: Optional[GroupOfLinesRefStructure] = field(
        default=None,
        metadata={
            "name": "GroupOfLinesRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    direction_name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "DirectionName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    external_line_ref: Optional[LineRefStructure] = field(
        default=None,
        metadata={
            "name": "ExternalLineRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    branding_ref_or_branding: Optional[Union[BrandingRefStructure, BrandingStructure]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "BrandingRef",
                    "type": BrandingRefStructure,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "Branding",
                    "type": BrandingStructure,
                    "namespace": "http://www.siri.org.uk/siri",
                },
            ),
        },
    )
    reason: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "Reason",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    extensions: Optional[Extensions1] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
