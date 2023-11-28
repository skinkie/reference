from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class TicketingFacilityEnumeration(Enum):
    """
    Allowed values for Ticketing Facility.
    """
    UNKNOWN = "unknown"
    TICKET_MACHINES = "ticketMachines"
    TICKET_OFFICE = "ticketOffice"
    TICKET_ON_DEMAND_MACHINES = "ticketOnDemandMachines"
    MOBILE_TICKETING = "mobileTicketing"
