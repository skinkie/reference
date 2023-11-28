from dataclasses import dataclass
from netex.parking_tariff_ref_structure import ParkingTariffRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ParkingTariffRef(ParkingTariffRefStructure):
    """
    Reference to a PARKING TARIFF.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
