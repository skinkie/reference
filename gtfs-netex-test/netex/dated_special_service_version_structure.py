from dataclasses import dataclass, field
from typing import Optional
from netex.dated_calls_rel_structure import DatedCallsRelStructure
from netex.dated_special_service_ref import DatedSpecialServiceRef
from netex.dated_vehicle_journey_ref import DatedVehicleJourneyRef
from netex.dead_run_ref import DeadRunRef
from netex.driver_ref import DriverRef
from netex.external_object_ref_structure import ExternalObjectRefStructure
from netex.journey_pattern_ref_structure import JourneyPatternRefStructure
from netex.operating_day_ref import OperatingDayRef
from netex.service_journey_ref import ServiceJourneyRef
from netex.single_journey_ref import SingleJourneyRef
from netex.special_service_ref import SpecialServiceRef
from netex.special_service_version_structure import SpecialServiceVersionStructure
from netex.target_passing_times_rel_structure import TargetPassingTimesRelStructure
from netex.template_service_journey_ref import TemplateServiceJourneyRef
from netex.vehicle_journey_ref import VehicleJourneyRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DatedSpecialServiceVersionStructure(SpecialServiceVersionStructure):
    """
    Type for DATED SPECIAL SERVICE.

    :ivar choice_1:
    :ivar operating_day_ref:
    :ivar external_dated_vehicle_journey_ref: An alternative  code that
        uniquely identifies theDATED  VEHICLE  JOURNEY. Specifically for
        use in AVMS systems. For VDV compatibility.
    :ivar dated_journey_pattern_ref: Reference to a JOURNEY PATTERN.
    :ivar driver_ref:
    :ivar dated_passing_times: PASSING TIMEs  for JOURNEY.
    :ivar dated_calls: DATED CALLs  for JOURNEY.
    """
    class Meta:
        name = "DatedSpecialService_VersionStructure"

    choice_1: Optional[object] = field(
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
        }
    )
    operating_day_ref: OperatingDayRef = field(
        metadata={
            "name": "OperatingDayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    external_dated_vehicle_journey_ref: Optional[ExternalObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "ExternalDatedVehicleJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    dated_journey_pattern_ref: Optional[JourneyPatternRefStructure] = field(
        default=None,
        metadata={
            "name": "DatedJourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    driver_ref: Optional[DriverRef] = field(
        default=None,
        metadata={
            "name": "DriverRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    dated_passing_times: Optional[TargetPassingTimesRelStructure] = field(
        default=None,
        metadata={
            "name": "datedPassingTimes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    dated_calls: Optional[DatedCallsRelStructure] = field(
        default=None,
        metadata={
            "name": "datedCalls",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
