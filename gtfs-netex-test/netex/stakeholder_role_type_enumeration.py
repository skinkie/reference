from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class StakeholderRoleTypeEnumeration(Enum):
    PLANNING = "planning"
    OPERATION = "operation"
    CONTROL = "control"
    RESERVATION = "reservation"
    ENTITY_LEGAL_OWNERSHIP = "entityLegalOwnership"
    FARE_MANAGEMENT = "fareManagement"
    FINANCING = "financing"
    SECURITY_MANAGEMENT = "securityManagement"
    CUSTOMER_SERVICE = "customerService"
    DATA_REGISTRAR = "dataRegistrar"
    TENANT = "tenant"
    FACILITY_MANAGEMENT = "facilityManagement"
    LESSOR = "lessor"
    OTHER = "other"
