from dataclasses import dataclass
from .delta_structure import DeltaStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Delta(DeltaStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
