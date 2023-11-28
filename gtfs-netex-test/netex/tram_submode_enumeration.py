from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class TramSubmodeEnumeration(Enum):
    """Values for Tram MODEs of TRANSPORT: TPEG pti_table_06, col_table_12."""
    UNKNOWN = "unknown"
    UNDEFINED = "undefined"
    CITY_TRAM = "cityTram"
    LOCAL_TRAM = "localTram"
    REGIONAL_TRAM = "regionalTram"
    SIGHTSEEING_TRAM = "sightseeingTram"
    SHUTTLE_TRAM = "shuttleTram"
    TRAIN_TRAM = "trainTram"
