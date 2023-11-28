from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class GroupOfLinesTypeEnumeration(Enum):
    """Allowed values Classification of GROUP of  LINEs.

    +v1.1

    :cvar MARKETING: Grouping is primarily for marketing purposes.
    :cvar ADMINISTRATIVE: Grouping is primarily for administrative
        purposes..
    :cvar SCHEDULING: Grouping is primarily for creating schedules
        purposes.
    :cvar CONTROL: Grouping is primarily for defining tariff scope.
    :cvar TARIFF: Grouping is primarily for defining tariff scope.
    :cvar OTHER:
    """
    MARKETING = "marketing"
    ADMINISTRATIVE = "administrative"
    SCHEDULING = "scheduling"
    CONTROL = "control"
    TARIFF = "tariff"
    OTHER = "other"
