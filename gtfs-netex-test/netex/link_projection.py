from dataclasses import dataclass
from .link_projection_version_structure import LinkProjectionVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LinkProjection(LinkProjectionVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
