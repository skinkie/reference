from dataclasses import dataclass, field
from typing import List, Optional, Union

from xsdata.models.datatype import XmlDuration

from .abstract_item_structure import AbstractItemStructure
from .branding_ref_structure import BrandingRefStructure
from .branding_structure import BrandingStructure
from .dated_vehicle_journey_structure import DatedVehicleJourneyStructure
from .direction_ref_structure import DirectionRefStructure
from .extensions_1 import Extensions1
from .first_or_last_journey_enumeration import FirstOrLastJourneyEnumeration
from .group_of_lines_ref_structure import GroupOfLinesRefStructure
from .journey_pattern_ref_structure import JourneyPatternRefStructure
from .line_ref_structure import LineRefStructure
from .natural_language_place_name_structure import NaturalLanguagePlaceNameStructure
from .natural_language_string_structure import NaturalLanguageStringStructure
from .operator_ref_structure import OperatorRefStructure
from .product_category_ref_structure import ProductCategoryRefStructure
from .published_line_name import PublishedLineName
from .removed_dated_vehicle_journey_structure import RemovedDatedVehicleJourneyStructure
from .removed_service_journey_interchange_structure import RemovedServiceJourneyInterchangeStructure
from .route_ref_structure import RouteRefStructure
from .service_feature_ref import ServiceFeatureRef
from .service_journey_interchange_structure import ServiceJourneyInterchangeStructure
from .timetable_validity_period import TimetableValidityPeriod
from .vehicle_feature_ref_structure import VehicleFeatureRefStructure
from .vehicle_modes_enumeration import VehicleModesEnumeration
from .version_ref_structure import VersionRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class DatedTimetableVersionFrameStructure(AbstractItemStructure):
    version_ref: Optional[VersionRefStructure] = field(
        default=None,
        metadata={
            "name": "VersionRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    validity_period: Optional[TimetableValidityPeriod] = field(
        default=None,
        metadata={
            "name": "ValidityPeriod",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    shortest_possible_cycle: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "ShortestPossibleCycle",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    line_ref: LineRefStructure = field(
        metadata={
            "name": "LineRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    direction_ref: DirectionRefStructure = field(
        metadata={
            "name": "DirectionRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
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
    operator_ref: Optional[OperatorRefStructure] = field(
        default=None,
        metadata={
            "name": "OperatorRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    product_category_ref: Optional[ProductCategoryRefStructure] = field(
        default=None,
        metadata={
            "name": "ProductCategoryRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    service_feature_ref: List[ServiceFeatureRef] = field(
        default_factory=list,
        metadata={
            "name": "ServiceFeatureRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    vehicle_feature_ref: List[VehicleFeatureRefStructure] = field(
        default_factory=list,
        metadata={
            "name": "VehicleFeatureRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    origin_display: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "OriginDisplay",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    destination_display: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "DestinationDisplay",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    line_note: List[NaturalLanguagePlaceNameStructure] = field(
        default_factory=list,
        metadata={
            "name": "LineNote",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    first_or_last_journey: Optional[FirstOrLastJourneyEnumeration] = field(
        default=None,
        metadata={
            "name": "FirstOrLastJourney",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    headway_service: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HeadwayService",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    monitored: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Monitored",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    dated_vehicle_journey: List[DatedVehicleJourneyStructure] = field(
        default_factory=list,
        metadata={
            "name": "DatedVehicleJourney",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    removed_dated_vehicle_journey: List[RemovedDatedVehicleJourneyStructure] = field(
        default_factory=list,
        metadata={
            "name": "RemovedDatedVehicleJourney",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    service_journey_interchange: List[ServiceJourneyInterchangeStructure] = field(
        default_factory=list,
        metadata={
            "name": "ServiceJourneyInterchange",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    removed_service_journey_interchange: List[RemovedServiceJourneyInterchangeStructure] = field(
        default_factory=list,
        metadata={
            "name": "RemovedServiceJourneyInterchange",
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
