from dataclasses import dataclass

from .level_in_structure_version_structure import LevelInStructureVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LevelInStructure(LevelInStructureVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
