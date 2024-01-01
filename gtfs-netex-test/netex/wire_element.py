from dataclasses import dataclass
from .wire_element_version_structure import WireElementVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class WireElement(WireElementVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
