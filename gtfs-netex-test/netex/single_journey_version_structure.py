from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlTime
from netex.car_pooling_service_ref import CarPoolingServiceRef
from netex.chauffeured_vehicle_service_ref import ChauffeuredVehicleServiceRef
from netex.journey_version_structure import JourneyVersionStructure
from netex.operating_day_ref import OperatingDayRef
from netex.single_journey_path_ref import SingleJourneyPathRef
from netex.target_passing_times_rel_structure import TargetPassingTimesRelStructure
from netex.taxi_service_ref import TaxiServiceRef
from netex.vehicle_meeting_point_assignments_rel_structure import VehicleMeetingPointAssignmentsRelStructure
from netex.vehicle_ref import VehicleRef
from netex.vehicle_rental_service_ref import VehicleRentalServiceRef
from netex.vehicle_sharing_service_ref import VehicleSharingServiceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SingleJourneyVersionStructure(JourneyVersionStructure):
    """
    Type for SINGLE JOURNEY.

    :ivar choice:
    :ivar vehicle_ref:
    :ivar single_journey_path_ref:
    :ivar departure_time: Departure time.
    :ivar departure_day_offset: Departure Time Day Offset
    :ivar operating_day_ref:
    :ivar dated_passing_times: DATED PASSING TIMEsfor SINGLE JOURNEY
    :ivar meeting_point_assignments: MEETING POINT ASSIGNMENTS for
        SINGLE JOURNEY
    """
    class Meta:
        name = "SingleJourney_VersionStructure"

    choice: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "VehicleRentalServiceRef",
                    "type": VehicleRentalServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleSharingServiceRef",
                    "type": VehicleSharingServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ChauffeuredVehicleServiceRef",
                    "type": ChauffeuredVehicleServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TaxiServiceRef",
                    "type": TaxiServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CarPoolingServiceRef",
                    "type": CarPoolingServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    vehicle_ref: Optional[VehicleRef] = field(
        default=None,
        metadata={
            "name": "VehicleRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    single_journey_path_ref: Optional[SingleJourneyPathRef] = field(
        default=None,
        metadata={
            "name": "SingleJourneyPathRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    departure_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "DepartureTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    departure_day_offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "DepartureDayOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    operating_day_ref: Optional[OperatingDayRef] = field(
        default=None,
        metadata={
            "name": "OperatingDayRef",
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
    meeting_point_assignments: Optional[VehicleMeetingPointAssignmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "meetingPointAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
