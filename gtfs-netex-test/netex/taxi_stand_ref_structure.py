from dataclasses import dataclass
from netex.quay_ref_structure import QuayRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TaxiStandRefStructure(QuayRefStructure):
    """
    Type for a reference to a TAXI STAND.
    """
