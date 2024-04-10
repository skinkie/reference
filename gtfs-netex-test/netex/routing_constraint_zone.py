from dataclasses import dataclass

from .routing_constraint_zone_version_structure import RoutingConstraintZoneVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RoutingConstraintZone(RoutingConstraintZoneVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
