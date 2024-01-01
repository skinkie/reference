from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class FlexibleOperationTypeEnumeration(Enum):
    FLEXIBLE_ROUTE = "flexibleRoute"
    FLEXIBLE_AREA = "flexibleArea"
    DEMAND_RESPONSIVE = "demandResponsive"
