from dataclasses import dataclass
from .quality_structure_factor_price_versioned_child_structure import (
    QualityStructureFactorPriceVersionedChildStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class QualityStructureFactorPrice(
    QualityStructureFactorPriceVersionedChildStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
