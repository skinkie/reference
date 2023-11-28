from dataclasses import dataclass
from netex.level_ref_structure import LevelRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class LevelRef(LevelRefStructure):
    """
    Reference to LEVEL of a SITE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
