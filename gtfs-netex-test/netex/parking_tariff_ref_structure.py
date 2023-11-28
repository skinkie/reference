from dataclasses import dataclass
from netex.tariff_ref_structure import TariffRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ParkingTariffRefStructure(TariffRefStructure):
    """
    Type for a reference to a PARKING TARIFF.
    """
