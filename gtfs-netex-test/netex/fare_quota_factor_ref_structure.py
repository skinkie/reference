from dataclasses import dataclass

from .quality_structure_factor_ref_structure import QualityStructureFactorRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class FareQuotaFactorRefStructure(QualityStructureFactorRefStructure):
    pass
