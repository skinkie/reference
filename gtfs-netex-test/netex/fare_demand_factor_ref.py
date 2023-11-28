from dataclasses import dataclass
from netex.fare_demand_factor_ref_structure import FareDemandFactorRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FareDemandFactorRef(FareDemandFactorRefStructure):
    """
    Reference to a FARE DEMAND FACTOR.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
