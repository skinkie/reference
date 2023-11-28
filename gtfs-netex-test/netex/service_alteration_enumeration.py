from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ServiceAlterationEnumeration(Enum):
    """
    Allowed values for Service Alteration.
    """
    EXTRA_JOURNEY = "extraJourney"
    CANCELLATION = "cancellation"
    PLANNED = "planned"
    REPLACED = "replaced"
