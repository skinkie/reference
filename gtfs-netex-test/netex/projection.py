from dataclasses import dataclass

from .projection_version_structure import ProjectionVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class Projection(ProjectionVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
