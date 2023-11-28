from dataclasses import dataclass
from netex.parking_charge_band_ref_structure import ParkingChargeBandRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ParkingChargeBandRef(ParkingChargeBandRefStructure):
    """
    Reference to a PARKING TARIFF CHARGE BAND.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
