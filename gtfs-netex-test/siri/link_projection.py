from dataclasses import dataclass

from .link_projection_structure import LinkProjectionStructure

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass(kw_only=True)
class LinkProjection(LinkProjectionStructure):
    class Meta:
        namespace = "http://www.ifopt.org.uk/ifopt"
