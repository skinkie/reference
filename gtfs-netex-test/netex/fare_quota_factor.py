from dataclasses import dataclass, field
from netex.fare_quota_factor_version_structure import FareQuotaFactorVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FareQuotaFactor(FareQuotaFactorVersionStructure):
    """A named set of parameters defining the number of quota fares available.

    of a given denomination.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
