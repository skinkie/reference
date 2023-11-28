from dataclasses import dataclass
from netex.parking_price_ref_structure import ParkingPriceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ParkingPriceRef(ParkingPriceRefStructure):
    """
    Reference to a PARKING TARIFF PRICE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
