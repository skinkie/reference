from dataclasses import dataclass
from .parking_charge_band_ref_structure import ParkingChargeBandRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ParkingChargeBandRef(ParkingChargeBandRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
