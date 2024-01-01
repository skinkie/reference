from dataclasses import dataclass
from .mode_ref_structure import ModeRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ModeRef(ModeRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
