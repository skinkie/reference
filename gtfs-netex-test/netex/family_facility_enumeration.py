from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class FamilyFacilityEnumeration(Enum):
    NONE = "none"
    SERVICES_FOR_CHILDREN = "servicesForChildren"
    SERVICES_FOR_ARMY_FAMILIES = "servicesForArmyFamilies"
    NURSERY_SERVICE = "nurseryService"
