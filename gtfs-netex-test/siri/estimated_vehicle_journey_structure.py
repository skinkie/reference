from dataclasses import dataclass, field
from typing import ForwardRef, List, Optional, Union

from xsdata.models.datatype import XmlDateTime, XmlDuration

from .block_ref_structure import BlockRefStructure
from .branding_ref_structure import BrandingRefStructure
from .branding_structure import BrandingStructure
from .compound_train import CompoundTrain
from .course_of_journey_ref_structure import CourseOfJourneyRefStructure
from .dated_vehicle_journey_indirect_ref_structure import DatedVehicleJourneyIndirectRefStructure
from .dated_vehicle_journey_ref_structure import DatedVehicleJourneyRefStructure
from .destination_ref import DestinationRef
from .direction_ref_structure import DirectionRefStructure
from .estimated_call import EstimatedCall
from .extensions_1 import Extensions1
from .facility_change_element import FacilityChangeElement
from .facility_condition_element import FacilityConditionElement
from .first_or_last_journey import FirstOrLastJourney
from .formation_condition import FormationCondition
from .framed_vehicle_journey_ref_structure import FramedVehicleJourneyRefStructure
from .group_of_lines_ref_structure import GroupOfLinesRefStructure
from .journey_note import JourneyNote
from .journey_part_info_structure import JourneyPartInfoStructure
from .journey_pattern_ref_structure import JourneyPatternRefStructure
from .journey_relations_structure import JourneyRelationsStructure
from .line_ref_structure import LineRefStructure
from .location_structure import LocationStructure
from .natural_language_place_name_structure import NaturalLanguagePlaceNameStructure
from .natural_language_string_structure import NaturalLanguageStringStructure
from .occupancy import Occupancy
from .operator_ref_structure import OperatorRefStructure
from .origin_ref import OriginRef
from .prediction_inaccurate import PredictionInaccurate
from .prediction_inaccurate_reason import PredictionInaccurateReason
from .product_category_ref_structure import ProductCategoryRefStructure
from .progress_rate_enumeration import ProgressRateEnumeration
from .published_line_name import PublishedLineName
from .quality_index_enumeration import QualityIndexEnumeration
from .recorded_call import RecordedCall
from .route_ref_structure import RouteRefStructure
from .service_feature_ref import ServiceFeatureRef
from .simple_contact_structure import SimpleContactStructure
from .situation_ref import SituationRef
from .train import Train
from .train_block_part_structure import TrainBlockPartStructure
from .train_element import TrainElement
from .train_element_ref import TrainElementRef
from .train_number_ref_structure import TrainNumberRefStructure
from .vehicle_feature_ref_structure import VehicleFeatureRefStructure
from .vehicle_journey_ref import VehicleJourneyRef
from .vehicle_modes_enumeration import VehicleModesEnumeration
from .vehicle_ref import VehicleRef
from .vehicle_status_enumeration import VehicleStatusEnumeration
from .via_name_structure import ViaNameStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class EstimatedVehicleJourneyStructure:
    recorded_at_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "RecordedAtTime",
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
    framed_vehicle_journey_ref_or_dated_vehicle_journey_ref_or_dated_vehicle_journey_indirect_ref_or_estimated_vehicle_journey_code: List[Union[FramedVehicleJourneyRefStructure, DatedVehicleJourneyRefStructure, DatedVehicleJourneyIndirectRefStructure, str]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FramedVehicleJourneyRef",
                    "type": FramedVehicleJourneyRefStructure,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "DatedVehicleJourneyRef",
                    "type": DatedVehicleJourneyRefStructure,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "DatedVehicleJourneyIndirectRef",
                    "type": DatedVehicleJourneyIndirectRefStructure,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "EstimatedVehicleJourneyCode",
                    "type": str,
                    "namespace": "http://www.siri.org.uk/siri",
                },
            ),
            "max_occurs": 2,
        },
    )
    extra_journey_or_cancellation: Optional[Union["EstimatedVehicleJourneyStructure.ExtraJourney", "EstimatedVehicleJourneyStructure.Cancellation"]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ExtraJourney",
                    "type": ForwardRef("EstimatedVehicleJourneyStructure.ExtraJourney"),
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "Cancellation",
                    "type": ForwardRef("EstimatedVehicleJourneyStructure.Cancellation"),
                    "namespace": "http://www.siri.org.uk/siri",
                },
            ),
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
    monitored: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Monitored",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    monitoring_error: List[str] = field(
        default_factory=list,
        metadata={
            "name": "MonitoringError",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "tokens": True,
        },
    )
    in_congestion: Optional[bool] = field(
        default=None,
        metadata={
            "name": "InCongestion",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    in_panic: Optional[bool] = field(
        default=None,
        metadata={
            "name": "InPanic",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    prediction_inaccurate: Optional[PredictionInaccurate] = field(
        default=None,
        metadata={
            "name": "PredictionInaccurate",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    prediction_inaccurate_reason: Optional[PredictionInaccurateReason] = field(
        default=None,
        metadata={
            "name": "PredictionInaccurateReason",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    data_source: Optional[str] = field(
        default=None,
        metadata={
            "name": "DataSource",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    confidence_level: Optional[QualityIndexEnumeration] = field(
        default=None,
        metadata={
            "name": "ConfidenceLevel",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    vehicle_location: Optional[LocationStructure] = field(
        default=None,
        metadata={
            "name": "VehicleLocation",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    location_recorded_at_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "LocationRecordedAtTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    bearing: Optional[float] = field(
        default=None,
        metadata={
            "name": "Bearing",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    progress_rate: Optional[ProgressRateEnumeration] = field(
        default=None,
        metadata={
            "name": "ProgressRate",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    velocity: Optional[int] = field(
        default=None,
        metadata={
            "name": "Velocity",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    engine_on: Optional[bool] = field(
        default=None,
        metadata={
            "name": "EngineOn",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    occupancy: Optional[Occupancy] = field(
        default=None,
        metadata={
            "name": "Occupancy",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    delay: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "Delay",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    progress_status: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "ProgressStatus",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    vehicle_status: Optional[VehicleStatusEnumeration] = field(
        default=None,
        metadata={
            "name": "VehicleStatus",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    train_block_part: List[TrainBlockPartStructure] = field(
        default_factory=list,
        metadata={
            "name": "TrainBlockPart",
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
    train_numbers: Optional["EstimatedVehicleJourneyStructure.TrainNumbers"] = field(
        default=None,
        metadata={
            "name": "TrainNumbers",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    journey_parts: Optional["EstimatedVehicleJourneyStructure.JourneyParts"] = field(
        default=None,
        metadata={
            "name": "JourneyParts",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    train_elements: Optional["EstimatedVehicleJourneyStructure.TrainElements"] = field(
        default=None,
        metadata={
            "name": "TrainElements",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    trains: Optional["EstimatedVehicleJourneyStructure.Trains"] = field(
        default=None,
        metadata={
            "name": "Trains",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    compound_trains: Optional["EstimatedVehicleJourneyStructure.CompoundTrains"] = field(
        default=None,
        metadata={
            "name": "CompoundTrains",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    recorded_calls: Optional["EstimatedVehicleJourneyStructure.RecordedCalls"] = field(
        default=None,
        metadata={
            "name": "RecordedCalls",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    estimated_calls: Optional["EstimatedVehicleJourneyStructure.EstimatedCalls"] = field(
        default=None,
        metadata={
            "name": "EstimatedCalls",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    is_complete_stop_sequence: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsCompleteStopSequence",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    journey_relations: Optional[JourneyRelationsStructure] = field(
        default=None,
        metadata={
            "name": "JourneyRelations",
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

    @dataclass(kw_only=True)
    class RecordedCalls:
        recorded_call: List[RecordedCall] = field(
            default_factory=list,
            metadata={
                "name": "RecordedCall",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )

    @dataclass(kw_only=True)
    class EstimatedCalls:
        estimated_call: List[EstimatedCall] = field(
            default_factory=list,
            metadata={
                "name": "EstimatedCall",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )

    @dataclass(kw_only=True)
    class TrainNumbers:
        train_number_ref: List[TrainNumberRefStructure] = field(
            default_factory=list,
            metadata={
                "name": "TrainNumberRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )

    @dataclass(kw_only=True)
    class JourneyParts:
        journey_part_info: List[JourneyPartInfoStructure] = field(
            default_factory=list,
            metadata={
                "name": "JourneyPartInfo",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )

    @dataclass(kw_only=True)
    class TrainElements:
        train_element_ref_or_train_element: List[Union[TrainElementRef, TrainElement]] = field(
            default_factory=list,
            metadata={
                "type": "Elements",
                "choices": (
                    {
                        "name": "TrainElementRef",
                        "type": TrainElementRef,
                        "namespace": "http://www.siri.org.uk/siri",
                    },
                    {
                        "name": "TrainElement",
                        "type": TrainElement,
                        "namespace": "http://www.siri.org.uk/siri",
                    },
                ),
            },
        )

    @dataclass(kw_only=True)
    class Trains:
        train_ref_or_train: List[Union[object, Train]] = field(
            default_factory=list,
            metadata={
                "type": "Elements",
                "choices": (
                    {
                        "name": "TrainRef",
                        "type": object,
                        "namespace": "http://www.siri.org.uk/siri",
                    },
                    {
                        "name": "Train",
                        "type": Train,
                        "namespace": "http://www.siri.org.uk/siri",
                    },
                ),
            },
        )

    @dataclass(kw_only=True)
    class CompoundTrains:
        compound_train_ref_or_compound_train: List[Union[object, CompoundTrain]] = field(
            default_factory=list,
            metadata={
                "type": "Elements",
                "choices": (
                    {
                        "name": "CompoundTrainRef",
                        "type": object,
                        "namespace": "http://www.siri.org.uk/siri",
                    },
                    {
                        "name": "CompoundTrain",
                        "type": CompoundTrain,
                        "namespace": "http://www.siri.org.uk/siri",
                    },
                ),
            },
        )

    @dataclass(kw_only=True)
    class ExtraJourney:
        value: bool = field(
            metadata={
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class Cancellation:
        value: bool = field(
            metadata={
                "required": True,
            }
        )
