from dataclasses import dataclass
from .link_projection_ref_structure import LinkProjectionRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LinkProjectionRef(LinkProjectionRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
