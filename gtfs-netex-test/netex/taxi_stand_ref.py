from dataclasses import dataclass
from netex.taxi_stand_ref_structure import TaxiStandRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TaxiStandRef(TaxiStandRefStructure):
    """Reference to a TAXI STAND.

    +v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
