from dataclasses import dataclass, field
from typing import Optional
from netex.quality_structure_factor_version_structure import QualityStructureFactorVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FareQuotaFactorVersionStructure(QualityStructureFactorVersionStructure):
    """
    Type for FARE QUOTA FACTOR.

    :ivar number_of_units: Number of units available of product at a
        given price.
    """
    class Meta:
        name = "FareQuotaFactor_VersionStructure"

    number_of_units: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfUnits",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
