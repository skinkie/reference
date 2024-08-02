from dataclasses import dataclass, field
from typing import ForwardRef, List, Optional, Union

from xsdata.models.datatype import XmlDateTime, XmlDuration

from .abstract_functional_service_request_structure import AbstractFunctionalServiceRequestStructure
from .access_modes_enumeration import AccessModesEnumeration
from .air_submode import AirSubmode
from .bus_submode import BusSubmode
from .coach_submode import CoachSubmode
from .connection_link_ref import ConnectionLinkRef
from .country_ref_structure import CountryRefStructure
from .extensions_1 import Extensions1
from .facility_ref import FacilityRef
from .framed_vehicle_journey_ref_structure import FramedVehicleJourneyRefStructure
from .half_open_timestamp_input_range_structure import HalfOpenTimestampInputRangeStructure
from .include_translations import IncludeTranslations
from .information_status_enum import InformationStatusEnum
from .interchange_ref import InterchangeRef
from .line_direction_structure import LineDirectionStructure
from .line_ref import LineRef
from .location_structure import LocationStructure
from .metro_submode import MetroSubmode
from .operational_unit_ref_structure import OperationalUnitRefStructure
from .operator_ref_structure import OperatorRefStructure
from .passenger_accessibility_needs_structure import PassengerAccessibilityNeedsStructure
from .predictability_enumeration import PredictabilityEnumeration
from .rail_submode import RailSubmode
from .road_filter_structure import RoadFilterStructure
from .scope_type_enumeration import ScopeTypeEnumeration
from .severity_enumeration import SeverityEnumeration
from .stop_place_ref_structure import StopPlaceRefStructure
from .stop_place_space_ref_structure import StopPlaceSpaceRefStructure
from .stop_point_ref import StopPointRef
from .telecabin_submode import TelecabinSubmode
from .tram_submode import TramSubmode
from .vehicle_journey_ref import VehicleJourneyRef
from .vehicle_mode import VehicleMode
from .vehicle_ref import VehicleRef
from .verification_status_enumeration import VerificationStatusEnumeration
from .water_submode import WaterSubmode
from .workflow_status_enumeration import WorkflowStatusEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class SituationExchangeRequestStructure(AbstractFunctionalServiceRequestStructure):
    preview_interval: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "PreviewInterval",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    start_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "StartTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    validity_period: Optional[HalfOpenTimestampInputRangeStructure] = field(
        default=None,
        metadata={
            "name": "ValidityPeriod",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    include_only_if_in_publication_window: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IncludeOnlyIfInPublicationWindow",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    vehicle_mode: Optional[VehicleMode] = field(
        default=None,
        metadata={
            "name": "VehicleMode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    air_submode_or_bus_submode_or_coach_submode_or_metro_submode_or_rail_submode_or_tram_submode_or_water_submode_or_telecabin_submode: Optional[Union[AirSubmode, BusSubmode, CoachSubmode, MetroSubmode, RailSubmode, TramSubmode, WaterSubmode, TelecabinSubmode]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AirSubmode",
                    "type": AirSubmode,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "BusSubmode",
                    "type": BusSubmode,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "CoachSubmode",
                    "type": CoachSubmode,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "MetroSubmode",
                    "type": MetroSubmode,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "RailSubmode",
                    "type": RailSubmode,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "TramSubmode",
                    "type": TramSubmode,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "WaterSubmode",
                    "type": WaterSubmode,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "TelecabinSubmode",
                    "type": TelecabinSubmode,
                    "namespace": "http://www.siri.org.uk/siri",
                },
            ),
        },
    )
    access_mode: Optional[AccessModesEnumeration] = field(
        default=None,
        metadata={
            "name": "AccessMode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    severity: Optional[SeverityEnumeration] = field(
        default=None,
        metadata={
            "name": "Severity",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    scope: List[ScopeTypeEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "Scope",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    predictability: Optional[PredictabilityEnumeration] = field(
        default=None,
        metadata={
            "name": "Predictability",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    keywords: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Keywords",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "tokens": True,
        },
    )
    verification: Optional[VerificationStatusEnumeration] = field(
        default=None,
        metadata={
            "name": "Verification",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    progress: List[WorkflowStatusEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "Progress",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    reality: Optional[InformationStatusEnum] = field(
        default=None,
        metadata={
            "name": "Reality",
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
    operational_unit_ref: List[OperationalUnitRefStructure] = field(
        default_factory=list,
        metadata={
            "name": "OperationalUnitRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    network_ref: Optional[OperatorRefStructure] = field(
        default=None,
        metadata={
            "name": "NetworkRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    line_ref_or_lines: List[Union[LineRef, "SituationExchangeRequestStructure.Lines"]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "LineRef",
                    "type": LineRef,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "Lines",
                    "type": ForwardRef("SituationExchangeRequestStructure.Lines"),
                    "namespace": "http://www.siri.org.uk/siri",
                },
            ),
        },
    )
    stop_point_ref: List[StopPointRef] = field(
        default_factory=list,
        metadata={
            "name": "StopPointRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    connection_link_ref: List[ConnectionLinkRef] = field(
        default_factory=list,
        metadata={
            "name": "ConnectionLinkRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    facility_ref: List[FacilityRef] = field(
        default_factory=list,
        metadata={
            "name": "FacilityRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_place_ref: Optional[StopPlaceRefStructure] = field(
        default=None,
        metadata={
            "name": "StopPlaceRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_place_component_ref: Optional[StopPlaceSpaceRefStructure] = field(
        default=None,
        metadata={
            "name": "StopPlaceComponentRef",
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
    interchange_ref: Optional[InterchangeRef] = field(
        default=None,
        metadata={
            "name": "InterchangeRef",
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
    country_ref: Optional[CountryRefStructure] = field(
        default=None,
        metadata={
            "name": "CountryRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    place_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlaceRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    location: List[LocationStructure] = field(
        default_factory=list,
        metadata={
            "name": "Location",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "max_occurs": 2,
        },
    )
    situation_road_filter: Optional["SituationExchangeRequestStructure.SituationRoadFilter"] = field(
        default=None,
        metadata={
            "name": "SituationRoadFilter",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    accessibility_need_filter: List[PassengerAccessibilityNeedsStructure] = field(
        default_factory=list,
        metadata={
            "name": "AccessibilityNeedFilter",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    language: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Language",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    include_translations: Optional[IncludeTranslations] = field(
        default=None,
        metadata={
            "name": "IncludeTranslations",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    maximum_number_of_situation_elements: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaximumNumberOfSituationElements",
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
    version: str = field(
        default="2.1",
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass(kw_only=True)
    class Lines:
        line_direction: List[LineDirectionStructure] = field(
            default_factory=list,
            metadata={
                "name": "LineDirection",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )

    @dataclass(kw_only=True)
    class SituationRoadFilter:
        road_filter: List[RoadFilterStructure] = field(
            default_factory=list,
            metadata={
                "name": "RoadFilter",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )
