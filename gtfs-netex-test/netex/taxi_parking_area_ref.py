from dataclasses import dataclass
from netex.taxi_parking_area_ref_structure import TaxiParkingAreaRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TaxiParkingAreaRef(TaxiParkingAreaRefStructure):
    """Reference to a TAXI PARKING AREA.

    +v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
