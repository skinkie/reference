from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SystemOfUnits(Enum):
    """
    System of units.

    :cvar SI_METRES: All measurements are SI metric. Distance = Metres
        Length = Metres Weight = Kilos Speed = Metres per second.
    :cvar SI_KILOMETRES_AND_METRES: All measurements are SI Distance =
        Kilometres Length = Metres Weight = Kilos Speed = Metres per
        second.
    :cvar OTHER:
    """
    SI_METRES = "SiMetres"
    SI_KILOMETRES_AND_METRES = "SiKilometresAndMetres"
    OTHER = "Other"
