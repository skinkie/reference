from dataclasses import dataclass

from .mode_ref_structure import ModeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ModeRef(ModeRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
