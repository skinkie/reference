from dataclasses import dataclass
from .direction_ref_structure import DirectionRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DirectionRef(DirectionRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
