from dataclasses import dataclass, field
from typing import List, Optional, Union

from xsdata.models.datatype import XmlDateTime

from .accessibility_assessment_structure import AccessibilityAssessmentStructure
from .affected_call_structure import AffectedCallStructure
from .affected_facility_structure import AffectedFacilityStructure
from .affected_operator_structure import AffectedOperatorStructure
from .affected_stop_point_structure import (
    AffectedRouteStructure,
    AffectedStopPointStructure,
)
from .block_ref_structure import BlockRefStructure
from .dated_vehicle_journey_ref_structure import DatedVehicleJourneyRefStructure
from .direction_ref_structure import DirectionRefStructure
from .extensions_1 import Extensions1
from .framed_vehicle_journey_ref_structure import FramedVehicleJourneyRefStructure
from .journey_part_info_structure import JourneyPartInfoStructure
from .line_ref_structure import LineRefStructure
from .natural_language_place_name_structure import NaturalLanguagePlaceNameStructure
from .natural_language_string_structure import NaturalLanguageStringStructure
from .published_line_name import PublishedLineName
from .service_condition_enumeration import ServiceConditionEnumeration
from .train_number_ref_structure import TrainNumberRefStructure
from .vehicle_journey_ref_structure import VehicleJourneyRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class AffectedVehicleJourneyStructure:
    framed_vehicle_journey_ref_or_vehicle_journey_ref: List[Union[FramedVehicleJourneyRefStructure, VehicleJourneyRefStructure]] = field(
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
                    "name": "VehicleJourneyRef",
                    "type": VehicleJourneyRefStructure,
                    "namespace": "http://www.siri.org.uk/siri",
                },
            ),
        },
    )
    dated_vehicle_journey_ref: List[DatedVehicleJourneyRefStructure] = field(
        default_factory=list,
        metadata={
            "name": "DatedVehicleJourneyRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    journey_name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "JourneyName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    operator: Optional[AffectedOperatorStructure] = field(
        default=None,
        metadata={
            "name": "Operator",
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
    published_line_name: List[PublishedLineName] = field(
        default_factory=list,
        metadata={
            "name": "PublishedLineName",
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
    block_ref: Optional[BlockRefStructure] = field(
        default=None,
        metadata={
            "name": "BlockRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    train_numbers: Optional["AffectedVehicleJourneyStructure.TrainNumbers"] = field(
        default=None,
        metadata={
            "name": "TrainNumbers",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    journey_parts: Optional["AffectedVehicleJourneyStructure.JourneyParts"] = field(
        default=None,
        metadata={
            "name": "JourneyParts",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    origins: List[AffectedStopPointStructure] = field(
        default_factory=list,
        metadata={
            "name": "Origins",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    destinations: List[AffectedStopPointStructure] = field(
        default_factory=list,
        metadata={
            "name": "Destinations",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    route: List[AffectedRouteStructure] = field(
        default_factory=list,
        metadata={
            "name": "Route",
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
    origin_display_at_destination: List[NaturalLanguagePlaceNameStructure] = field(
        default_factory=list,
        metadata={
            "name": "OriginDisplayAtDestination",
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
    accessibility_assessment: Optional[AccessibilityAssessmentStructure] = field(
        default=None,
        metadata={
            "name": "AccessibilityAssessment",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    journey_condition: List[ServiceConditionEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "JourneyCondition",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    calls: Optional["AffectedVehicleJourneyStructure.Calls"] = field(
        default=None,
        metadata={
            "name": "Calls",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    facilities: Optional["AffectedVehicleJourneyStructure.Facilities"] = field(
        default=None,
        metadata={
            "name": "Facilities",
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
    class Calls:
        call: List[AffectedCallStructure] = field(
            default_factory=list,
            metadata={
                "name": "Call",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )

    @dataclass(kw_only=True)
    class Facilities:
        affected_facility: List[AffectedFacilityStructure] = field(
            default_factory=list,
            metadata={
                "name": "AffectedFacility",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )
