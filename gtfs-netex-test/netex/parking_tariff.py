from dataclasses import dataclass
from .parking_tariff_version_structure import ParkingTariffVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ParkingTariff(ParkingTariffVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
