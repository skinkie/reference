from dataclasses import dataclass
from .replacing_version_structure import ReplacingVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Replacing(ReplacingVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
