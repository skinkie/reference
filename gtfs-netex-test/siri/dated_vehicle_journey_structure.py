from dataclasses import dataclass, field
from typing import ForwardRef, List, Optional, Union

from .block_ref_structure import BlockRefStructure
from .branding_ref_structure import BrandingRefStructure
from .branding_structure import BrandingStructure
from .compound_train import CompoundTrain
from .course_of_journey_ref_structure import CourseOfJourneyRefStructure
from .dated_call import DatedCall
from .dated_journey_part_info_structure import DatedJourneyPartInfoStructure
from .destination_ref import DestinationRef
from .extensions_1 import Extensions1
from .first_or_last_journey_enumeration import FirstOrLastJourneyEnumeration
from .framed_vehicle_journey_ref_structure import FramedVehicleJourneyRefStructure
from .group_of_lines_ref_structure import GroupOfLinesRefStructure
from .journey_note import JourneyNote
from .journey_pattern_ref_structure import JourneyPatternRefStructure
from .journey_relations_structure import JourneyRelationsStructure
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
from .train import Train
from .train_block_part_structure import TrainBlockPartStructure
from .train_element import TrainElement
from .train_element_ref import TrainElementRef
from .train_number_ref_structure import TrainNumberRefStructure
from .vehicle_feature_ref_structure import VehicleFeatureRefStructure
from .vehicle_journey_ref import VehicleJourneyRef
from .vehicle_modes_enumeration import VehicleModesEnumeration
from .vehicle_ref import VehicleRef
from .via_name_structure import ViaNameStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class DatedVehicleJourneyStructure:
    dated_vehicle_journey_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "DatedVehicleJourneyCode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    framed_vehicle_journey_ref_or_vehicle_journey_ref: Optional[Union[FramedVehicleJourneyRefStructure, VehicleJourneyRef]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FramedVehicleJourneyRef",
                    "type": FramedVehicleJourneyRefStructure,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "VehicleJourneyRef",
                    "type": VehicleJourneyRef,
                    "namespace": "http://www.siri.org.uk/siri",
                },
            ),
        },
    )
    extra_journey_or_cancellation: Optional[Union["DatedVehicleJourneyStructure.ExtraJourney", "DatedVehicleJourneyStructure.Cancellation"]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ExtraJourney",
                    "type": ForwardRef("DatedVehicleJourneyStructure.ExtraJourney"),
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "Cancellation",
                    "type": ForwardRef("DatedVehicleJourneyStructure.Cancellation"),
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
    vehicle_ref: Optional[VehicleRef] = field(
        default=None,
        metadata={
            "name": "VehicleRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    train_numbers: Optional["DatedVehicleJourneyStructure.TrainNumbers"] = field(
        default=None,
        metadata={
            "name": "TrainNumbers",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    journey_parts: Optional["DatedVehicleJourneyStructure.JourneyParts"] = field(
        default=None,
        metadata={
            "name": "JourneyParts",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    train_elements: Optional["DatedVehicleJourneyStructure.TrainElements"] = field(
        default=None,
        metadata={
            "name": "TrainElements",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    trains: Optional["DatedVehicleJourneyStructure.Trains"] = field(
        default=None,
        metadata={
            "name": "Trains",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    compound_trains: Optional["DatedVehicleJourneyStructure.CompoundTrains"] = field(
        default=None,
        metadata={
            "name": "CompoundTrains",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    dated_calls: "DatedVehicleJourneyStructure.DatedCalls" = field(
        metadata={
            "name": "DatedCalls",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
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
    class DatedCalls:
        dated_call: List[DatedCall] = field(
            default_factory=list,
            metadata={
                "name": "DatedCall",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 2,
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
        journey_part_info: List[DatedJourneyPartInfoStructure] = field(
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
