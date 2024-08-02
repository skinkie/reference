from dataclasses import dataclass, field
from typing import List, Optional, Union

from xsdata.models.datatype import XmlDateTime

from .block_ref_structure import BlockRefStructure
from .branding_ref_structure import BrandingRefStructure
from .branding_structure import BrandingStructure
from .course_of_journey_ref_structure import CourseOfJourneyRefStructure
from .destination_ref import DestinationRef
from .direction_ref_structure import DirectionRefStructure
from .extensions_1 import Extensions1
from .facility_change_element import FacilityChangeElement
from .facility_condition_element import FacilityConditionElement
from .first_or_last_journey import FirstOrLastJourney
from .formation_condition import FormationCondition
from .framed_vehicle_journey_ref_structure import FramedVehicleJourneyRefStructure
from .group_of_lines_ref_structure import GroupOfLinesRefStructure
from .journey_note import JourneyNote
from .journey_pattern_ref_structure import JourneyPatternRefStructure
from .line_ref_structure import LineRefStructure
from .natural_language_place_name_structure import NaturalLanguagePlaceNameStructure
from .natural_language_string_structure import NaturalLanguageStringStructure
from .operator_ref_structure import OperatorRefStructure
from .origin_ref import OriginRef
from .product_category_ref_structure import ProductCategoryRefStructure
from .published_line_name import PublishedLineName
from .route_ref_structure import RouteRefStructure
from .service_feature_ref import ServiceFeatureRef
from .simple_contact_structure import SimpleContactStructure
from .situation_ref import SituationRef
from .vehicle_feature_ref_structure import VehicleFeatureRefStructure
from .vehicle_journey_ref import VehicleJourneyRef
from .vehicle_modes_enumeration import VehicleModesEnumeration
from .vehicle_ref import VehicleRef
from .via_name_structure import ViaNameStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class InterchangeJourneyStructure:
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
    framed_vehicle_journey_ref: Optional[FramedVehicleJourneyRefStructure] = field(
        default=None,
        metadata={
            "name": "FramedVehicleJourneyRef",
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
    origin_ref: Optional[OriginRef] = field(
        default=None,
        metadata={
            "name": "OriginRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    origin_name: List[NaturalLanguagePlaceNameStructure] = field(
        default_factory=list,
        metadata={
            "name": "OriginName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    origin_short_name: List[NaturalLanguagePlaceNameStructure] = field(
        default_factory=list,
        metadata={
            "name": "OriginShortName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    destination_display_at_origin: List[NaturalLanguagePlaceNameStructure] = field(
        default_factory=list,
        metadata={
            "name": "DestinationDisplayAtOrigin",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    via: List[ViaNameStructure] = field(
        default_factory=list,
        metadata={
            "name": "Via",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    destination_ref: Optional[DestinationRef] = field(
        default=None,
        metadata={
            "name": "DestinationRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    destination_name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "DestinationName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    destination_short_name: List[NaturalLanguagePlaceNameStructure] = field(
        default_factory=list,
        metadata={
            "name": "DestinationShortName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    origin_display_at_destination: List[NaturalLanguagePlaceNameStructure] = field(
        default_factory=list,
        metadata={
            "name": "OriginDisplayAtDestination",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    vehicle_journey_name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "VehicleJourneyName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    journey_note: List[JourneyNote] = field(
        default_factory=list,
        metadata={
            "name": "JourneyNote",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    public_contact: Optional[SimpleContactStructure] = field(
        default=None,
        metadata={
            "name": "PublicContact",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    operations_contact: Optional[SimpleContactStructure] = field(
        default=None,
        metadata={
            "name": "OperationsContact",
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
    origin_aimed_departure_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "OriginAimedDepartureTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    destination_aimed_arrival_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DestinationAimedArrivalTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    first_or_last_journey: Optional[FirstOrLastJourney] = field(
        default=None,
        metadata={
            "name": "FirstOrLastJourney",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    formation_condition: List[FormationCondition] = field(
        default_factory=list,
        metadata={
            "name": "FormationCondition",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    facility_condition_element: List[FacilityConditionElement] = field(
        default_factory=list,
        metadata={
            "name": "FacilityConditionElement",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    facility_change_element: Optional[FacilityChangeElement] = field(
        default=None,
        metadata={
            "name": "FacilityChangeElement",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    situation_ref: List[SituationRef] = field(
        default_factory=list,
        metadata={
            "name": "SituationRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    block_ref: Optional[BlockRefStructure] = field(
        default=None,
        metadata={
            "name": "BlockRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    course_of_journey_ref: Optional[CourseOfJourneyRefStructure] = field(
        default=None,
        metadata={
            "name": "CourseOfJourneyRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    vehicle_journey_ref: Optional[VehicleJourneyRef] = field(
        default=None,
        metadata={
            "name": "VehicleJourneyRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    vehicle_ref: Optional[VehicleRef] = field(
        default=None,
        metadata={
            "name": "VehicleRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    additional_vehicle_journey_ref: List[FramedVehicleJourneyRefStructure] = field(
        default_factory=list,
        metadata={
            "name": "AdditionalVehicleJourneyRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    driver_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "DriverRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    driver_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "DriverName",
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
    aimed_departure_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "AimedDepartureTime",
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
