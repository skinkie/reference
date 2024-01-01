from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ServiceAlterationEnumeration(Enum):
    EXTRA_JOURNEY = "extraJourney"
    CANCELLATION = "cancellation"
    PLANNED = "planned"
    REPLACED = "replaced"
