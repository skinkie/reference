from dataclasses import dataclass

from .fare_demand_factor_ref_structure import FareDemandFactorRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class FareDemandFactorRef(FareDemandFactorRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
