from dataclasses import dataclass, field
from typing import List, Optional
from netex.address_ref import AddressRef
from netex.boarding_position_ref import BoardingPositionRef
from netex.parking_ref import ParkingRef
from netex.point_of_interest_ref import PointOfInterestRef
from netex.postal_address_ref import PostalAddressRef
from netex.quay_ref import QuayRef
from netex.road_address_ref import RoadAddressRef
from netex.scheduled_stop_point_view import ScheduledStopPointView
from netex.service_site_ref import ServiceSiteRef
from netex.site_ref import SiteRef
from netex.stop_place_ref import StopPlaceRef
from netex.tariff_zone_ref import TariffZoneRef
from netex.taxi_rank_ref import TaxiRankRef
from netex.taxi_stand_ref import TaxiStandRef
from netex.topographic_place_view import TopographicPlaceView
from netex.vehicle_meeting_point_ref import VehicleMeetingPointRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TravelSpecificationSummaryEndpointStructure:
    """
    Origin or destnation elements for TRAVEL SPECIFICATION Summary View.
    """
    topographic_place_view: Optional[TopographicPlaceView] = field(
        default=None,
        metadata={
            "name": "TopographicPlaceView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    choice: Optional[object] = field(
        default=None,
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
                    "name": "ParkingRef",
                    "type": ParkingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointOfInterestRef",
                    "type": PointOfInterestRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceSiteRef",
                    "type": ServiceSiteRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SiteRef",
                    "type": SiteRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    postal_address_ref_or_road_address_ref_or_address_ref: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "PostalAddressRef",
                    "type": PostalAddressRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoadAddressRef",
                    "type": RoadAddressRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AddressRef",
                    "type": AddressRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    scheduled_stop_point_view: Optional[ScheduledStopPointView] = field(
        default=None,
        metadata={
            "name": "ScheduledStopPointView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_meeting_point_ref: Optional[VehicleMeetingPointRef] = field(
        default=None,
        metadata={
            "name": "VehicleMeetingPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    taxi_stand_ref_or_quay_ref: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
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
            ),
        }
    )
    boarding_position_ref: Optional[BoardingPositionRef] = field(
        default=None,
        metadata={
            "name": "BoardingPositionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    tariff_zone_ref: List[TariffZoneRef] = field(
        default_factory=list,
        metadata={
            "name": "TariffZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
