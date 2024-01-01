from dataclasses import dataclass
from .line_link_ref_structure import LineLinkRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LineLinkRef(LineLinkRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
