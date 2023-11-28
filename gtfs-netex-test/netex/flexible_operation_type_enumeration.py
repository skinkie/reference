from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class FlexibleOperationTypeEnumeration(Enum):
    """
    Allowed values for FlexibleModeOfOperation.
    """
    FLEXIBLE_ROUTE = "flexibleRoute"
    FLEXIBLE_AREA = "flexibleArea"
    DEMAND_RESPONSIVE = "demandResponsive"
