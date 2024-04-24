from dataclasses import dataclass, field
from typing import ForwardRef, List, Optional, Union

from xsdata.models.datatype import XmlDuration, XmlTime

from .booking_access_enumeration import BookingAccessEnumeration
from .booking_arrangements_rel_structure import BookingArrangementsRelStructure
from .booking_method_enumeration import BookingMethodEnumeration
from .contact_structure import ContactStructure
from .dated_special_service_ref import DatedSpecialServiceRef
from .dated_vehicle_journey_ref import DatedVehicleJourneyRef
from .dead_run_ref import DeadRunRef
from .entity_in_version_structure import DataManagedObjectStructure
from .flexible_service_enumeration import FlexibleServiceEnumeration
from .info_link_structure import InfoLinkStructure
from .multilingual_string import MultilingualString
from .normal_dated_vehicle_journey_ref import NormalDatedVehicleJourneyRef
from .purchase_moment_enumeration import PurchaseMomentEnumeration
from .purchase_when_enumeration import PurchaseWhenEnumeration
from .service_journey_ref import ServiceJourneyRef
from .single_journey_ref import SingleJourneyRef
from .special_service_ref import SpecialServiceRef
from .template_service_journey_ref import TemplateServiceJourneyRef
from .type_of_flexible_service_ref import TypeOfFlexibleServiceRef
from .vehicle_journey_ref import VehicleJourneyRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FlexibleServicePropertiesVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "FlexibleServiceProperties_VersionStructure"

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
            "FlexibleServicePropertiesVersionStructure.MinimumBookingPeriod",
            "FlexibleServicePropertiesVersionStructure.MaximumBookingPeriod",
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
                    "type": ForwardRef("FlexibleServicePropertiesVersionStructure.MinimumBookingPeriod"),
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MaximumBookingPeriod",
                    "type": ForwardRef("FlexibleServicePropertiesVersionStructure.MaximumBookingPeriod"),
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
