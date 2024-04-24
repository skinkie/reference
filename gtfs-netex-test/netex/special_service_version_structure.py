from dataclasses import dataclass, field
from typing import ForwardRef, List, Optional, Union

from xsdata.models.datatype import XmlDuration, XmlTime

from .booking_access_enumeration import BookingAccessEnumeration
from .booking_arrangements_rel_structure import BookingArrangementsRelStructure
from .booking_method_enumeration import BookingMethodEnumeration
from .compound_train_ref import CompoundTrainRef
from .contact_structure import ContactStructure
from .day_type_refs_rel_structure import DayTypeRefsRelStructure
from .dead_run_journey_pattern_ref import DeadRunJourneyPatternRef
from .dynamic_advertisement_enumeration import DynamicAdvertisementEnumeration
from .flexible_service_enumeration import FlexibleServiceEnumeration
from .frequency_structure import FrequencyStructure
from .info_link_structure import InfoLinkStructure
from .journey_endpoint_structure import JourneyEndpointStructure
from .journey_pattern_ref import JourneyPatternRef
from .journey_version_structure import JourneyVersionStructure
from .multilingual_string import MultilingualString
from .powered_train_ref import PoweredTrainRef
from .purchase_moment_enumeration import PurchaseMomentEnumeration
from .purchase_when_enumeration import PurchaseWhenEnumeration
from .service_journey_pattern_ref import ServiceJourneyPatternRef
from .service_pattern_ref import ServicePatternRef
from .train_ref import TrainRef
from .type_of_flexible_service_ref import TypeOfFlexibleServiceRef
from .unpowered_train_ref import UnpoweredTrainRef
from .vehicle_type_ref import VehicleTypeRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SpecialServiceVersionStructure(JourneyVersionStructure):
    class Meta:
        name = "SpecialService_VersionStructure"

    departure_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "DepartureTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    departure_day_offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "DepartureDayOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    frequency: Optional[FrequencyStructure] = field(
        default=None,
        metadata={
            "name": "Frequency",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    journey_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "JourneyDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    client: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Client",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    day_types: Optional[DayTypeRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "dayTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    journey_pattern_ref: Optional[Union[ServiceJourneyPatternRef, ServicePatternRef, DeadRunJourneyPatternRef, JourneyPatternRef]] = field(
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
        },
    )
    vehicle_type_ref_or_train_ref: Optional[Union[CompoundTrainRef, UnpoweredTrainRef, PoweredTrainRef, TrainRef, VehicleTypeRef]] = field(
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
                    "name": "UnpoweredTrainRef",
                    "type": UnpoweredTrainRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PoweredTrainRef",
                    "type": PoweredTrainRef,
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
        },
    )
    origin: Optional[JourneyEndpointStructure] = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    destination: Optional[JourneyEndpointStructure] = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    print: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Print",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    dynamic: Optional[DynamicAdvertisementEnumeration] = field(
        default=None,
        metadata={
            "name": "Dynamic",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_flexible_service_ref: Optional[TypeOfFlexibleServiceRef] = field(
        default=None,
        metadata={
            "name": "TypeOfFlexibleServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    flexible_service_type: Optional[FlexibleServiceEnumeration] = field(
        default=None,
        metadata={
            "name": "FlexibleServiceType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    cancellation_possible: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CancellationPossible",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    change_of_time_possible: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ChangeOfTimePossible",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    choice: List[
        Union[
            BookingArrangementsRelStructure,
            ContactStructure,
            List[BookingMethodEnumeration],
            BookingAccessEnumeration,
            PurchaseWhenEnumeration,
            List[PurchaseMomentEnumeration],
            XmlTime,
            "SpecialServiceVersionStructure.MinimumBookingPeriod",
            "SpecialServiceVersionStructure.MaximumBookingPeriod",
            InfoLinkStructure,
            MultilingualString,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "bookingArrangements",
                    "type": BookingArrangementsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BookingContact",
                    "type": ContactStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BookingMethods",
                    "type": List[BookingMethodEnumeration],
                    "namespace": "http://www.netex.org.uk/netex",
                    "default_factory": list,
                    "tokens": True,
                },
                {
                    "name": "BookingAccess",
                    "type": BookingAccessEnumeration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BookWhen",
                    "type": PurchaseWhenEnumeration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BuyWhen",
                    "type": List[PurchaseMomentEnumeration],
                    "namespace": "http://www.netex.org.uk/netex",
                    "default_factory": list,
                    "tokens": True,
                },
                {
                    "name": "LatestBookingTime",
                    "type": XmlTime,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MinimumBookingPeriod",
                    "type": ForwardRef("SpecialServiceVersionStructure.MinimumBookingPeriod"),
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MaximumBookingPeriod",
                    "type": ForwardRef("SpecialServiceVersionStructure.MaximumBookingPeriod"),
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BookingUrl",
                    "type": InfoLinkStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BookingNote",
                    "type": MultilingualString,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
            "max_occurs": 10,
        },
    )

    @dataclass(kw_only=True)
    class MaximumBookingPeriod:
        value: XmlDuration = field(
            metadata={
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class MinimumBookingPeriod:
        value: XmlDuration = field(
            metadata={
                "required": True,
            }
        )
