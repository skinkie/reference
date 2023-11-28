from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class TaxiSubmodeEnumeration(Enum):
    """Values for Taxi MODEs of TRANSPORT: TPEG pti_table_11."""
    UNKNOWN = "unknown"
    UNDEFINED = "undefined"
    COMMUNAL_TAXI = "communalTaxi"
    CHARTER_TAXI = "charterTaxi"
    WATER_TAXI = "waterTaxi"
    RAIL_TAXI = "railTaxi"
    BIKE_TAXI = "bikeTaxi"
    BLACK_CAB = "blackCab"
    MINI_CAB = "miniCab"
    APP_TAXI = "appTaxi"
    FIACRE = "fiacre"
    RICKSHAW = "rickshaw"
    CYCLE_RICKSHAW = "cycleRickshaw"
    ALL_TAXI_SERVICES = "allTaxiServices"
