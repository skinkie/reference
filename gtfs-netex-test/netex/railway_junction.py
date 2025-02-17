from dataclasses import dataclass

from .railway_junction_version_structure import RailwayJunctionVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class RailwayJunction(RailwayJunctionVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
