from enum import Enum

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


class CheckPointServiceEnumeration(Enum):
    SELFSERVICE_MACHINE = "selfserviceMachine"
    COUNTER_SERVICE = "counterService"
    OTHER = "other"
