from dataclasses import dataclass
from .tariff_ref_structure import TariffRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ParkingTariffRefStructure(TariffRefStructure):
    value: RestrictedVar
