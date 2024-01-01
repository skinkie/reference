from dataclasses import dataclass
from .parking_tariff_ref_structure import ParkingTariffRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ParkingTariffRef(ParkingTariffRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
