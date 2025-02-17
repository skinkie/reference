from dataclasses import dataclass

from .quality_structure_factor_version_structure import QualityStructureFactorVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class QualityStructureFactor(QualityStructureFactorVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
