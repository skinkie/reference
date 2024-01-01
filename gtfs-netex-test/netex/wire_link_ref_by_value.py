from dataclasses import dataclass
from .wire_link_ref_by_value_structure import WireLinkRefByValueStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class WireLinkRefByValue(WireLinkRefByValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
