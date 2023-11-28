from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class StakeholderRoleTypeEnumeration(Enum):
    """
    Allowed values for Stakeholder Roles.
    """
    PLANNING = "Planning"
    OPERATION = "Operation"
    CONTROL = "Control"
    RESERVATION = "Reservation"
    ENTITY_LEGAL_OWNERSHIP = "EntityLegalOwnership"
    FARE_MANAGEMENT = "FareManagement"
    FINANCING = "Financing"
    SECURITY_MANAGEMENT = "SecurityManagement"
    CUSTOMER_SERVICE = "CustomerService"
    DATA_REGISTRAR = "DataRegistrar"
    OTHER = "Other"
