from dataclasses import dataclass

from .projection_ref_structure import ProjectionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class LinkProjectionRefStructure(ProjectionRefStructure):
    pass
