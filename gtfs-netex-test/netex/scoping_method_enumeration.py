from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ScopingMethodEnumeration(Enum):
    """
    Allowed values for FARE ZONE Scoping Method.

    :cvar EXPLICIT_STOPS: Stops that are members of the zone are
        explicitly listed.
    :cvar IMPLICIT_SPATIAL_PROJECTION: Any stop that is spatially
        contained within the zone is assumed to be a  member.
    :cvar EXPLICIT_PERIPHERY_STOPS: The extent of the zone is indicated
        by a set of stops marking the border points on the periphery of
        the FARE ZONE. Any stop that is spatially contained within the
        indicated zone is assumed to be a  member.
    :cvar OTHER: Other method
    """
    EXPLICIT_STOPS = "explicitStops"
    IMPLICIT_SPATIAL_PROJECTION = "implicitSpatialProjection"
    EXPLICIT_PERIPHERY_STOPS = "explicitPeripheryStops"
    OTHER = "other"
