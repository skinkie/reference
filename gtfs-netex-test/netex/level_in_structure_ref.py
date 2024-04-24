from dataclasses import dataclass

from .level_in_structure_ref_structure import LevelInStructureRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LevelInStructureRef(LevelInStructureRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
