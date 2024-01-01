from dataclasses import dataclass
from .direction_value_structure import DirectionValueStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Direction(DirectionValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
