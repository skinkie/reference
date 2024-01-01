from dataclasses import dataclass
from .fare_demand_factor_version_structure import (
    FareDemandFactorVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareDemandFactor(FareDemandFactorVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
