from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SnowAndIceSubmodeEnumeration(Enum):
    """
    Values for Snow and Ice SUBMODEs of TRANSPORT.
    """
    UNKNOWN = "unknown"
    UNDEFINED = "undefined"
    SNOW_MOBILE = "snowMobile"
    SNOW_CAT = "snowCat"
    SNOW_COACH = "snowCoach"
    TERRA_BUS = "terraBus"
    WIND_SLED = "windSled"
