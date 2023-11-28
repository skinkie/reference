from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDuration, XmlTime
from netex.booking_access_enumeration import BookingAccessEnumeration
from netex.booking_method_enumeration import BookingMethodEnumeration
from netex.compound_train_ref import CompoundTrainRef
from netex.contact_structure import ContactStructure
from netex.day_type_refs_rel_structure import DayTypeRefsRelStructure
from netex.dead_run_journey_pattern_ref import DeadRunJourneyPatternRef
from netex.dynamic_advertisement_enumeration import DynamicAdvertisementEnumeration
from netex.flexible_service_enumeration import FlexibleServiceEnumeration
from netex.frequency_structure import FrequencyStructure
from netex.journey_endpoint_structure import JourneyEndpointStructure
from netex.journey_pattern_ref import JourneyPatternRef
from netex.journey_version_structure import JourneyVersionStructure
from netex.multilingual_string import MultilingualString
from netex.purchase_moment_enumeration import PurchaseMomentEnumeration
from netex.purchase_when_enumeration import PurchaseWhenEnumeration
from netex.service_journey_pattern_ref import ServiceJourneyPatternRef
from netex.service_pattern_ref import ServicePatternRef
from netex.train_ref import TrainRef
from netex.type_of_flexible_service_ref import TypeOfFlexibleServiceRef
from netex.vehicle_type_ref import VehicleTypeRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SpecialServiceVersionStructure(JourneyVersionStructure):
    """
    Type for SPECIAL SERVICE.

    :ivar departure_time: Time of departure.
    :ivar departure_day_offset: Day offset if day of departure time of
        VEHICLE JOURNEY differs from the current OPERATING DAY.
    :ivar frequency: Frequency of Journey.
    :ivar journey_duration: Total length of Journey. Can be computed
        from individual times.  Add to Departure time to obtain JOURNEY
        arrival time.
    :ivar client: Client of Special Service.
    :ivar day_types: DAY TYPEs for Journey.
    :ivar choice:
    :ivar compound_train_ref_or_train_ref_or_vehicle_type_ref:
    :ivar origin: Origin  for JOURNEY.
    :ivar destination: Destination  for JOURNEY.
    :ivar print: Whether the journey is included in printed media.
        Default is true.
    :ivar dynamic: When SERVICE JOURNEY is to be publicised in dynamic
        media. Default is always.
    :ivar type_of_flexible_service_ref:
    :ivar flexible_service_type: Flexible service type is
        FixedPassingTimes/DynamicPassingTimes/FixedHeadwayFrequency (in
        the last value, this provides a maximum waiting time, but no
        passing time is defined, all is done dynamically depending on
        the demand). A NotFlexible value is probably also required to
        clearly state that a Stop (i.e. Point in JP) is not flexible
        when others are.
    :ivar cancellation_possible: Whether cancellation is always possible
        (meaning the Operator can decided to cancel, usually because
        there are not enough people, or they are too busy to run
        service).
    :ivar change_of_time_possible: Whether the time of the service may
        be altered.
    :ivar booking_contact: Contact for Booking. +v1.1
    :ivar booking_methods: Allowed Ways of Making a BOOKING.
    :ivar booking_access: Who can make a booking. Default is public.
    :ivar book_when: When Booking can be made. +V1.1
    :ivar buy_when: When purchase can be made.  +V1.1
    :ivar latest_booking_time: Latest time in day that booking can be
        made.
    :ivar minimum_booking_period: Minimum interval in advance of
        departure day or time that Service may be ordered.
    :ivar maximum_booking_period: Maximum interval in advance of
        departure day or time that Service may be ordered. +V1.2..2
    :ivar booking_url: URL for booking. +V1.1
    :ivar booking_note: Note about booking the FLEXIBLE LINE.
    """
    class Meta:
        name = "SpecialService_VersionStructure"

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
    frequency: Optional[FrequencyStructure] = field(
        default=None,
        metadata={
            "name": "Frequency",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    journey_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "JourneyDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    client: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Client",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    day_types: Optional[DayTypeRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "dayTypes",
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
                    "name": "ServiceJourneyPatternRef",
                    "type": ServiceJourneyPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServicePatternRef",
                    "type": ServicePatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DeadRunJourneyPatternRef",
                    "type": DeadRunJourneyPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyPatternRef",
                    "type": JourneyPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    compound_train_ref_or_train_ref_or_vehicle_type_ref: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "CompoundTrainRef",
                    "type": CompoundTrainRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainRef",
                    "type": TrainRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleTypeRef",
                    "type": VehicleTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    origin: Optional[JourneyEndpointStructure] = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    destination: Optional[JourneyEndpointStructure] = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    print: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Print",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    dynamic: Optional[DynamicAdvertisementEnumeration] = field(
        default=None,
        metadata={
            "name": "Dynamic",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_flexible_service_ref: Optional[TypeOfFlexibleServiceRef] = field(
        default=None,
        metadata={
            "name": "TypeOfFlexibleServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    flexible_service_type: Optional[FlexibleServiceEnumeration] = field(
        default=None,
        metadata={
            "name": "FlexibleServiceType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    cancellation_possible: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CancellationPossible",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    change_of_time_possible: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ChangeOfTimePossible",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    booking_contact: Optional[ContactStructure] = field(
        default=None,
        metadata={
            "name": "BookingContact",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    booking_methods: List[BookingMethodEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "BookingMethods",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    booking_access: Optional[BookingAccessEnumeration] = field(
        default=None,
        metadata={
            "name": "BookingAccess",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    book_when: Optional[PurchaseWhenEnumeration] = field(
        default=None,
        metadata={
            "name": "BookWhen",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    buy_when: List[PurchaseMomentEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "BuyWhen",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    latest_booking_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "LatestBookingTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    minimum_booking_period: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MinimumBookingPeriod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximum_booking_period: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MaximumBookingPeriod",
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
    booking_note: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "BookingNote",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
