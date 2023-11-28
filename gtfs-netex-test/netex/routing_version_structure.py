from dataclasses import dataclass, field
from typing import Optional
from netex.usage_parameter_version_structure import UsageParameterVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RoutingVersionStructure(UsageParameterVersionStructure):
    """
    Type for ROUTING.

    :ivar is_restricted: Whether restricted to certain toutes.
    :ivar return_route_identical: Whether return must be same as
        outward.
    :ivar forwards_only: Passenger may only take routes that proceed in
        a single direction. (They may not use product to achieve a
        return trip for the cost of a single trip by purchasing a
        circular route and a making a journe break).
    :ivar cross_border: Whether route crosses a border.
    """
    class Meta:
        name = "Routing_VersionStructure"

    is_restricted: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsRestricted",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    return_route_identical: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ReturnRouteIdentical",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    forwards_only: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ForwardsOnly",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    cross_border: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CrossBorder",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
