from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ScheduledOperationTypeEnumeration(Enum):
    """
    Allowed values for ScheduledOperationModeOfOperation.
    """
    SCHEDULED_SERVICE = "scheduledService"
    EVENT_BASED_SERVICE = "eventBasedService"
