from dataclasses import dataclass
from netex.time_structure_factor_ref_structure import TimeStructureFactorRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ParkingChargeBandRefStructure(TimeStructureFactorRefStructure):
    """
    Type for a reference to a PARKING TARIFF CHARGE BAND.
    """
