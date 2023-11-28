from dataclasses import dataclass, field
from typing import List, Optional
from netex.access_space_ref import AccessSpaceRef
from netex.all_vehicle_modes_of_transport_enumeration import AllVehicleModesOfTransportEnumeration
from netex.authority_ref import AuthorityRef
from netex.boarding_position_ref import BoardingPositionRef
from netex.multilingual_string import MultilingualString
from netex.operator_ref import OperatorRef
from netex.operator_view import OperatorView
from netex.parking_area_ref import ParkingAreaRef
from netex.parking_entrance_for_vehicles_ref import ParkingEntranceForVehiclesRef
from netex.parking_entrance_ref import ParkingEntranceRef
from netex.parking_passenger_entrance_ref import ParkingPassengerEntranceRef
from netex.parking_ref import ParkingRef
from netex.point_of_interest_entrance_ref import PointOfInterestEntranceRef
from netex.point_of_interest_ref import PointOfInterestRef
from netex.point_of_interest_space_ref import PointOfInterestSpaceRef
from netex.point_ref_structure import PointRefStructure
from netex.quay_ref import QuayRef
from netex.scheduled_stop_point_ref_structure import ScheduledStopPointRefStructure
from netex.stop_area_ref_structure import StopAreaRefStructure
from netex.stop_place_entrance_ref import StopPlaceEntranceRef
from netex.stop_place_ref import StopPlaceRef
from netex.taxi_parking_area_ref import TaxiParkingAreaRef
from netex.taxi_rank_ref import TaxiRankRef
from netex.taxi_stand_ref import TaxiStandRef
from netex.vehicle_pooling_parking_area_ref import VehiclePoolingParkingAreaRef
from netex.vehicle_sharing_parking_area_ref import VehicleSharingParkingAreaRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SiteConnectionEndStructure:
    """
    Type for a SITE CONNECTION End.

    :ivar transport_mode: MODE of end point of TRANSFER . Default is all
        modes, i.e. all modes of referenced stop place and or stop
        point.
    :ivar stop_area_ref: Identifier of a Place at end point of transfer.
    :ivar scheduled_stop_point_ref_or_vehicle_meeting_point_ref:
    :ivar choice:
    :ivar authority_ref_or_operator_ref_or_operator_view:
    :ivar label: Label at end of site connection.
    """
    transport_mode: Optional[AllVehicleModesOfTransportEnumeration] = field(
        default=None,
        metadata={
            "name": "TransportMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    stop_area_ref: Optional[StopAreaRefStructure] = field(
        default=None,
        metadata={
            "name": "StopAreaRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    scheduled_stop_point_ref_or_vehicle_meeting_point_ref: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ScheduledStopPointRef",
                    "type": ScheduledStopPointRefStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleMeetingPointRef",
                    "type": PointRefStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TaxiRankRef",
                    "type": TaxiRankRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StopPlaceRef",
                    "type": StopPlaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AccessSpaceRef",
                    "type": AccessSpaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BoardingPositionRef",
                    "type": BoardingPositionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TaxiStandRef",
                    "type": TaxiStandRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "QuayRef",
                    "type": QuayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StopPlaceEntranceRef",
                    "type": StopPlaceEntranceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointOfInterestRef",
                    "type": PointOfInterestRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointOfInterestSpaceRef",
                    "type": PointOfInterestSpaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointOfInterestEntranceRef",
                    "type": PointOfInterestEntranceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingRef",
                    "type": ParkingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehiclePoolingParkingAreaRef",
                    "type": VehiclePoolingParkingAreaRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleSharingParkingAreaRef",
                    "type": VehicleSharingParkingAreaRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TaxiParkingAreaRef",
                    "type": TaxiParkingAreaRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingAreaRef",
                    "type": ParkingAreaRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingEntranceForVehiclesRef",
                    "type": ParkingEntranceForVehiclesRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingPassengerEntranceRef",
                    "type": ParkingPassengerEntranceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingEntranceRef",
                    "type": ParkingEntranceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
            "max_occurs": 8,
        }
    )
    authority_ref_or_operator_ref_or_operator_view: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AuthorityRef",
                    "type": AuthorityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OperatorRef",
                    "type": OperatorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OperatorView",
                    "type": OperatorView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    label: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Label",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
