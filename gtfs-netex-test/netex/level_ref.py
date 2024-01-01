from dataclasses import dataclass
from .level_ref_structure import LevelRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LevelRef(LevelRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
