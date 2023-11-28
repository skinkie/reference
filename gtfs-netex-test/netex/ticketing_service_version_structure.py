from dataclasses import dataclass, field
from typing import List, Optional
from netex.local_service_version_structure import LocalServiceVersionStructure
from netex.payment_method_enumeration import PaymentMethodEnumeration
from netex.ticket_type_enumeration import TicketTypeEnumeration
from netex.ticketing_service_facility_enumeration import TicketingServiceFacilityEnumeration
from netex.vehicle_mode_enumeration import VehicleModeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TicketingServiceVersionStructure(LocalServiceVersionStructure):
    """
    Type for Ticketing Service.

    :ivar vehicle_modes: Modes for which TICKETING SERVICEs apply.
    :ivar ticketing_service_list: Service available.
    :ivar ticket_type_list: Ticket Types available.
    :ivar ticket_counter_service: Whether there is a ticket counter
        staffed by humans.
    :ivar online_purchase_for_collection: Whether there is online
        purchase for collection.
    :ivar online_purchase_for_eticket: Whether there is online purchase
        for eticket.
    :ivar online_purchase_for_self_print_ticket: Whether there is online
        purchase for self print.
    :ivar mobile_device_tickets: Whether there is mobile device tickets.
    :ivar payment_methods: Method of payment allowed.
    """
    class Meta:
        name = "TicketingService_VersionStructure"

    vehicle_modes: List[VehicleModeEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "VehicleModes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    ticketing_service_list: List[TicketingServiceFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "TicketingServiceList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    ticket_type_list: List[List[TicketTypeEnumeration]] = field(
        default_factory=list,
        metadata={
            "name": "TicketTypeList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    ticket_counter_service: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TicketCounterService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    online_purchase_for_collection: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OnlinePurchaseForCollection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    online_purchase_for_eticket: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OnlinePurchaseForETicket",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    online_purchase_for_self_print_ticket: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OnlinePurchaseForSelfPrintTicket",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    mobile_device_tickets: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MobileDeviceTickets",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
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
