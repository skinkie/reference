from dataclasses import dataclass
from .cell_versioned_child_structure import FareStructureFactorVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareStructureFactor(FareStructureFactorVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
