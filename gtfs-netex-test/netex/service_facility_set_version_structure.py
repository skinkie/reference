from dataclasses import dataclass, field
from typing import List, Optional
from netex.accommodation_access_enumeration import AccommodationAccessEnumeration
from netex.accommodation_facility_enumeration import AccommodationFacilityEnumeration
from netex.accommodations_rel_structure import AccommodationsRelStructure
from netex.boarding_permission_enumeration import BoardingPermissionEnumeration
from netex.booking_process_enumeration import BookingProcessEnumeration
from netex.couchette_facility_enumeration import CouchetteFacilityEnumeration
from netex.facility_set_version_structure import FacilitySetVersionStructure
from netex.group_booking_enumeration import GroupBookingEnumeration
from netex.luggage_carriage_enumeration import LuggageCarriageEnumeration
from netex.onboard_stays_rel_structure import OnboardStaysRelStructure
from netex.reservation_enumeration import ReservationEnumeration
from netex.uic_product_characteristic_enumeration import UicProductCharacteristicEnumeration
from netex.uic_rate_type_enumeration import UicRateTypeEnumeration
from netex.vehicle_access_facility_enumeration import VehicleAccessFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ServiceFacilitySetVersionStructure(FacilitySetVersionStructure):
    """
    Type for a SERVICE FACILITY.

    :ivar vehicle_access_facility_list: List of Vehicle Access
        FACILITies. +v1.1
    :ivar accommodation_access_list: List of ACCOMMODATION Access
        rights.
    :ivar accommodation_facility_list: List of Accommodation FACILITies.
    :ivar boarding_permission:
    :ivar booking_process_facility_list:
    :ivar couchette_facility_list:
    :ivar group_booking_facility:
    :ivar luggage_carriage_facility_list:
    :ivar service_reservation_facility_list:
    :ivar uic_product_characteristic_list:
    :ivar uic_train_rate:
    :ivar accommodations: Accommodation available on service.
    :ivar onboard_stays: Permission to stay on board the service.
    """
    class Meta:
        name = "ServiceFacilitySet_VersionStructure"

    vehicle_access_facility_list: List[VehicleAccessFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "VehicleAccessFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    accommodation_access_list: List[AccommodationAccessEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "AccommodationAccessList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    accommodation_facility_list: List[AccommodationFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "AccommodationFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    boarding_permission: Optional[BoardingPermissionEnumeration] = field(
        default=None,
        metadata={
            "name": "BoardingPermission",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    booking_process_facility_list: List[BookingProcessEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "BookingProcessFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    couchette_facility_list: List[CouchetteFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "CouchetteFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    group_booking_facility: Optional[GroupBookingEnumeration] = field(
        default=None,
        metadata={
            "name": "GroupBookingFacility",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    luggage_carriage_facility_list: List[LuggageCarriageEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "LuggageCarriageFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    service_reservation_facility_list: List[ReservationEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "ServiceReservationFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    uic_product_characteristic_list: List[UicProductCharacteristicEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "UicProductCharacteristicList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    uic_train_rate: Optional[UicRateTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "UicTrainRate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    accommodations: Optional[AccommodationsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    onboard_stays: Optional[OnboardStaysRelStructure] = field(
        default=None,
        metadata={
            "name": "onboardStays",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
