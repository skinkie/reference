from dataclasses import dataclass

from .delta_structure import DeltaStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class Delta(DeltaStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
