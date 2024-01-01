from dataclasses import dataclass
from .taxi_stand_version_structure import TaxiStandVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TaxiStand(TaxiStandVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
