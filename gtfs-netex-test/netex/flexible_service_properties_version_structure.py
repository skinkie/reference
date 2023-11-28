from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDuration, XmlTime
from netex.alternative_texts_rel_structure import DataManagedObjectStructure
from netex.booking_access_enumeration import BookingAccessEnumeration
from netex.booking_method_enumeration import BookingMethodEnumeration
from netex.contact_structure import ContactStructure
from netex.dated_special_service_ref import DatedSpecialServiceRef
from netex.dated_vehicle_journey_ref import DatedVehicleJourneyRef
from netex.dead_run_ref import DeadRunRef
from netex.flexible_service_enumeration import FlexibleServiceEnumeration
from netex.multilingual_string import MultilingualString
from netex.purchase_moment_enumeration import PurchaseMomentEnumeration
from netex.purchase_when_enumeration import PurchaseWhenEnumeration
from netex.service_journey_ref import ServiceJourneyRef
from netex.single_journey_ref import SingleJourneyRef
from netex.special_service_ref import SpecialServiceRef
from netex.template_service_journey_ref import TemplateServiceJourneyRef
from netex.type_of_flexible_service_ref import TypeOfFlexibleServiceRef
from netex.vehicle_journey_ref import VehicleJourneyRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FlexibleServicePropertiesVersionStructure(DataManagedObjectStructure):
    """
    Type for FLEXIBLE SERVICE PROPERTies.

    :ivar choice:
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
        name = "FlexibleServiceProperties_VersionStructure"

    choice: Optional[object] = field(
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
