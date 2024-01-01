from dataclasses import dataclass
from .quality_structure_factor_ref_structure import (
    QualityStructureFactorRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareQuotaFactorRefStructure(QualityStructureFactorRefStructure):
    value: RestrictedVar
