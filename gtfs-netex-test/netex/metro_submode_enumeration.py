from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class MetroSubmodeEnumeration(Enum):
    """Values for Metro MODEs of TRANSPORT: TPEG pti_table_04."""
    UNKNOWN = "unknown"
    UNDEFINED = "undefined"
    METRO = "metro"
    TUBE = "tube"
    URBAN_RAILWAY = "urbanRailway"
