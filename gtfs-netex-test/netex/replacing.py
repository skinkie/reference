from dataclasses import dataclass

from .replacing_version_structure import ReplacingVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class Replacing(ReplacingVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
