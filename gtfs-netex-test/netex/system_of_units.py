from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SystemOfUnits(Enum):
    SI_METRES = "SiMetres"
    SI_KILOMETRES_AND_METRES = "SiKilometresAndMetres"
    OTHER = "Other"
