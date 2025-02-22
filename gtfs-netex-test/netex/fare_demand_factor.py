from dataclasses import dataclass

from .fare_demand_factor_version_structure import FareDemandFactorVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class FareDemandFactor(FareDemandFactorVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
