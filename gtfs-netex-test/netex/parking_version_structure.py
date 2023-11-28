from dataclasses import dataclass, field
from typing import List, Optional
from netex.accesses_rel_structure import AccessesRelStructure
from netex.multilingual_string import MultilingualString
from netex.navigation_paths_rel_structure import NavigationPathsRelStructure
from netex.parking_areas_rel_structure import ParkingAreasRelStructure
from netex.parking_entrances_for_vehicles_rel_structure import ParkingEntrancesForVehiclesRelStructure
from netex.parking_layout_enumeration import ParkingLayoutEnumeration
from netex.parking_payment_process_enumeration import ParkingPaymentProcessEnumeration
from netex.parking_properties_rel_structure import ParkingPropertiesRelStructure
from netex.parking_reservation_enumeration import ParkingReservationEnumeration
from netex.parking_type_enumeration import ParkingTypeEnumeration
from netex.parking_vehicle_enumeration import ParkingVehicleEnumeration
from netex.path_junctions_rel_structure import PathJunctionsRelStructure
from netex.payment_by_mobile_structure import PaymentByMobileStructure
from netex.payment_method_enumeration import PaymentMethodEnumeration
from netex.site_path_links_rel_structure import SitePathLinksRelStructure
from netex.site_version_structure import SiteVersionStructure
from netex.transport_type_refs_rel_structure import TransportTypeRefsRelStructure
from netex.type_of_parking_ref import TypeOfParkingRef
from netex.type_of_payment_method_refs_rel_structure import TypeOfPaymentMethodRefsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ParkingVersionStructure(SiteVersionStructure):
    """
    Type for a PARKING.

    :ivar path_links: PATH LINKs for SITE.
    :ivar path_junctions: PATH JUNCTIONs within the SITE and or between
        the SITE elsewhere.
    :ivar accesses: ACCESS links for SITE.
    :ivar navigation_paths: NAVIGATION PATHs within the SITE and or
        between the SITE elsewhere.
    :ivar public_code: Short public code for passengers to use when
        uniquely identifying the stop by SMS and other self-service
        channels.
    :ivar label: Additional Label of PARKING.
    :ivar parking_type: Type of PARKING.
    :ivar type_of_parking_ref:
    :ivar parking_vehicle_types: Types of Vehicle allowed in PARKING.
    :ivar vehicle_types: TRANSPORT TYPEs  that may use PARKING - open
        codes.  +v1.2.2
    :ivar parking_layout: Format of building.
    :ivar number_of_parking_levels: Total number of levels.
    :ivar principal_capacity: Number of parking places normamally
        available excluding special spaces, reserved spaces etc.
    :ivar total_capacity: Total number of parking places including
        disabled spaces etc.
    :ivar overnight_parking_permitted: Whether Overnight Parking is
        permitted.
    :ivar prohibited_for_hazardous_materials: Whether parking of
        vehicles containing hazardous materials is prohibited. Default
        is true.
    :ivar recharging_available: Whether car park has recharging points.
    :ivar secure: Whether Parking is offered as secure.
    :ivar real_time_occupancy_available: Whether Real-time occupancy
        data is normally available.
    :ivar parking_payment_process: Payment Process for use of PARKING.
    :ivar payment_methods: Method of Payment for use of PARKING.
    :ivar types_of_payment_method: Method of Payment - open values.
        =V1.1
    :ivar default_currency: Default Currency for payment.
    :ivar currencies_accepted: Currencies accepted.
    :ivar cards_accepted: Cards accepted.
    :ivar parking_reservation: Reservation facilities for PARKING.
    :ivar booking_url: URL to make booking.
    :ivar payment_by_mobile: How to make payment by phone.
    :ivar free_parking_out_of_hours: Whether there is free parking out
        of hours.
    :ivar parking_properties: Properties of PARKING.
    :ivar parking_areas: PARKING AREAs within PARKING.
    :ivar vehicle_entrances: VEHICLE ENTRANCEs within PARKING.
    """
    class Meta:
        name = "Parking_VersionStructure"

    path_links: Optional[SitePathLinksRelStructure] = field(
        default=None,
        metadata={
            "name": "pathLinks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    path_junctions: Optional[PathJunctionsRelStructure] = field(
        default=None,
        metadata={
            "name": "pathJunctions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    accesses: Optional[AccessesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    navigation_paths: Optional[NavigationPathsRelStructure] = field(
        default=None,
        metadata={
            "name": "navigationPaths",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    public_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PublicCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
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
    parking_type: Optional[ParkingTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "ParkingType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_parking_ref: Optional[TypeOfParkingRef] = field(
        default=None,
        metadata={
            "name": "TypeOfParkingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parking_vehicle_types: List[ParkingVehicleEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "ParkingVehicleTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    vehicle_types: Optional[TransportTypeRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "vehicleTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parking_layout: Optional[ParkingLayoutEnumeration] = field(
        default=None,
        metadata={
            "name": "ParkingLayout",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    number_of_parking_levels: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfParkingLevels",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    principal_capacity: Optional[int] = field(
        default=None,
        metadata={
            "name": "PrincipalCapacity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    total_capacity: Optional[int] = field(
        default=None,
        metadata={
            "name": "TotalCapacity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    overnight_parking_permitted: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OvernightParkingPermitted",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    prohibited_for_hazardous_materials: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ProhibitedForHazardousMaterials",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    recharging_available: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RechargingAvailable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    secure: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Secure",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    real_time_occupancy_available: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RealTimeOccupancyAvailable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parking_payment_process: List[ParkingPaymentProcessEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "ParkingPaymentProcess",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    payment_methods: List[PaymentMethodEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "PaymentMethods",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    types_of_payment_method: Optional[TypeOfPaymentMethodRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "typesOfPaymentMethod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    default_currency: Optional[str] = field(
        default=None,
        metadata={
            "name": "DefaultCurrency",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_length": 3,
            "max_length": 3,
            "pattern": r"[A-Z][A-Z][A-Z]",
        }
    )
    currencies_accepted: List[str] = field(
        default_factory=list,
        metadata={
            "name": "CurrenciesAccepted",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_length": 3,
            "max_length": 3,
            "pattern": r"[A-Z][A-Z][A-Z]",
            "tokens": True,
        }
    )
    cards_accepted: List[str] = field(
        default_factory=list,
        metadata={
            "name": "CardsAccepted",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    parking_reservation: Optional[ParkingReservationEnumeration] = field(
        default=None,
        metadata={
            "name": "ParkingReservation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    booking_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "BookingUrl",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    payment_by_mobile: Optional[PaymentByMobileStructure] = field(
        default=None,
        metadata={
            "name": "PaymentByMobile",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    free_parking_out_of_hours: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FreeParkingOutOfHours",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parking_properties: Optional[ParkingPropertiesRelStructure] = field(
        default=None,
        metadata={
            "name": "parkingProperties",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parking_areas: Optional[ParkingAreasRelStructure] = field(
        default=None,
        metadata={
            "name": "parkingAreas",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_entrances: Optional[ParkingEntrancesForVehiclesRelStructure] = field(
        default=None,
        metadata={
            "name": "vehicleEntrances",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
