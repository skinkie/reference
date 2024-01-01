from dataclasses import dataclass
from .interchanging_version_structure import InterchangingVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Interchanging(InterchangingVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
