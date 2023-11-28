from dataclasses import dataclass
from netex.routing_constraint_zone_ref_structure import RoutingConstraintZoneRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RoutingConstraintZoneRef(RoutingConstraintZoneRefStructure):
    """
    Reference to a ROUTING CONSTRAINT ZONE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
