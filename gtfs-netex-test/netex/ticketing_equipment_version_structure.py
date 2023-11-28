from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional
from netex.all_modes_enumeration import AllModesEnumeration
from netex.passenger_equipment_version_structure import PassengerEquipmentVersionStructure
from netex.payment_method_enumeration import PaymentMethodEnumeration
from netex.queue_management_enumeration import QueueManagementEnumeration
from netex.scope_of_ticket_enumeration import ScopeOfTicketEnumeration
from netex.ticket_type_enumeration import TicketTypeEnumeration
from netex.ticketing_facility_enumeration import TicketingFacilityEnumeration
from netex.ticketing_service_facility_enumeration import TicketingServiceFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TicketingEquipmentVersionStructure(PassengerEquipmentVersionStructure):
    """
    Type for a TICKETING EQUIPMENT.

    :ivar vehicle_modes: Modes for which ticketing services apply.
    :ivar ticket_machines: Whether there are ticket machines.
    :ivar number_of_machines: Number of ticket machines.
    :ivar height_of_machine_interface: Height of the ticket machine
        interface. +v1.1
    :ivar ticketing_facility_list:
    :ivar ticketing_service_facility_list:
    :ivar ticket_office: Whether there is a distinct ticket office.
    :ivar ticket_counter: Whether there is a ticket counter.
    :ivar number_of_tills: Number of ticket windows.
    :ivar queue_management: Queue management.
    :ivar payment_methods: Payment methods allowed.
    :ivar ticket_types_available: Types of Ticket available.
    :ivar scope_of_tickets_available: Scope of Ticket available.
    :ivar low_counter_access: Whether there is a low counter for
        accessibility.
    :ivar height_of_low_counter: Height of counter for accessibility.
    :ivar induction_loops: Whether there are induction loops.
    :ivar tactile_interface_available: Indicates whether there is a
        tactile interface +v1.1.
    :ivar audio_interface_available: Indicates whether there is an
        accessible audio interface (allowing a use closed eyes). +v1.1
    :ivar disabled_priority: Indicates a priority access for disabled
        (no-queue). +v1.1
    :ivar wheelchair_suitable: Indicates whether equipment may be used
        while seated in a wheelchair. +v1.1
    """
    class Meta:
        name = "TicketingEquipment_VersionStructure"

    vehicle_modes: List[AllModesEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "VehicleModes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    ticket_machines: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TicketMachines",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    number_of_machines: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfMachines",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    height_of_machine_interface: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "HeightOfMachineInterface",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    ticketing_facility_list: List[TicketingFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "TicketingFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    ticketing_service_facility_list: List[TicketingServiceFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "TicketingServiceFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    ticket_office: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TicketOffice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    ticket_counter: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TicketCounter",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    number_of_tills: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfTills",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    queue_management: Optional[QueueManagementEnumeration] = field(
        default=None,
        metadata={
            "name": "QueueManagement",
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
    ticket_types_available: List[TicketTypeEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "TicketTypesAvailable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    scope_of_tickets_available: List[ScopeOfTicketEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "ScopeOfTicketsAvailable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    low_counter_access: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LowCounterAccess",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    height_of_low_counter: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "HeightOfLowCounter",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    induction_loops: Optional[bool] = field(
        default=None,
        metadata={
            "name": "InductionLoops",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    tactile_interface_available: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TactileInterfaceAvailable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    audio_interface_available: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AudioInterfaceAvailable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    disabled_priority: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DisabledPriority",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    wheelchair_suitable: Optional[bool] = field(
        default=None,
        metadata={
            "name": "WheelchairSuitable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
