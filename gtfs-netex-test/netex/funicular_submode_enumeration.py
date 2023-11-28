from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class FunicularSubmodeEnumeration(Enum):
    """Values for Funicular MODEs of TRANSPORT: TPEG pti_table_10."""
    UNKNOWN = "unknown"
    FUNICULAR = "funicular"
    STREET_CABLE_CAR = "streetCableCar"
    ALL_FUNICULAR_SERVICES = "allFunicularServices"
    UNDEFINED_FUNICULAR = "undefinedFunicular"
