from dataclasses import dataclass, field
from typing import Optional, Union

from .calls_rel_structure import CallsRelStructure
from .dated_special_service_ref import DatedSpecialServiceRef
from .dated_vehicle_journey_ref import DatedVehicleJourneyRef
from .dead_run_ref import DeadRunRef
from .driver_ref import DriverRef
from .external_object_ref_structure import ExternalObjectRefStructure
from .journey_pattern_ref_structure import JourneyPatternRefStructure
from .normal_dated_vehicle_journey_ref import NormalDatedVehicleJourneyRef
from .operating_day_ref import OperatingDayRef
from .operating_day_view import OperatingDayView
from .replaced_journeys_rel_structure import ReplacedJourneysRelStructure
from .service_alteration_enumeration import ServiceAlterationEnumeration
from .service_journey_ref import ServiceJourneyRef
from .single_journey_ref import SingleJourneyRef
from .special_service_ref import SpecialServiceRef
from .target_passing_times_rel_structure import TargetPassingTimesRelStructure
from .template_service_journey_ref import TemplateServiceJourneyRef
from .uic_operating_period import UicOperatingPeriod
from .vehicle_journey_ref import VehicleJourneyRef
from .vehicle_journey_version_structure import VehicleJourneyVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class NormalDatedVehicleJourneyVersionStructure(VehicleJourneyVersionStructure):
    class Meta:
        name = "NormalDatedVehicleJourney_VersionStructure"

    journey_ref_or_special_service_ref_or_service_journey_ref_or_vehicle_journey_ref: Optional[Union[SingleJourneyRef, NormalDatedVehicleJourneyRef, DatedVehicleJourneyRef, DatedSpecialServiceRef, SpecialServiceRef, TemplateServiceJourneyRef, ServiceJourneyRef, DeadRunRef, VehicleJourneyRef]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "SingleJourneyRef",
                    "type": SingleJourneyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "NormalDatedVehicleJourneyRef",
                    "type": NormalDatedVehicleJourneyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DatedVehicleJourneyRef",
                    "type": DatedVehicleJourneyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DatedSpecialServiceRef",
                    "type": DatedSpecialServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SpecialServiceRef",
                    "type": SpecialServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TemplateServiceJourneyRef",
                    "type": TemplateServiceJourneyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceJourneyRef",
                    "type": ServiceJourneyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DeadRunRef",
                    "type": DeadRunRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleJourneyRef",
                    "type": VehicleJourneyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    replaced_journeys: Optional[ReplacedJourneysRelStructure] = field(
        default=None,
        metadata={
            "name": "replacedJourneys",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    operating_day_ref_or_operating_day_view: Optional[Union[OperatingDayRef, OperatingDayView]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "OperatingDayRef",
                    "type": OperatingDayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OperatingDayView",
                    "type": OperatingDayView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    uic_operating_period: Optional[UicOperatingPeriod] = field(
        default=None,
        metadata={
            "name": "UicOperatingPeriod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    external_dated_vehicle_journey_ref: Optional[ExternalObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "ExternalDatedVehicleJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    dated_journey_pattern_ref: Optional[JourneyPatternRefStructure] = field(
        default=None,
        metadata={
            "name": "DatedJourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    driver_ref: Optional[DriverRef] = field(
        default=None,
        metadata={
            "name": "DriverRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    dated_passing_times: Optional[TargetPassingTimesRelStructure] = field(
        default=None,
        metadata={
            "name": "datedPassingTimes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    dated_calls: Optional[CallsRelStructure] = field(
        default=None,
        metadata={
            "name": "datedCalls",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    service_alteration_type: Optional[ServiceAlterationEnumeration] = field(
        default=None,
        metadata={
            "name": "ServiceAlterationType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
