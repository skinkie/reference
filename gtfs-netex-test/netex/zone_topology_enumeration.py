from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ZoneTopologyEnumeration(Enum):
    """
    Allowed values for Fare Zone Topology.

    :cvar OVERLAPPING: Zones are of arbitrary shape and may overlap.
    :cvar HONEYCOMB: Zones are arranged as a tiled honeycomb of regular
        polygons (e.g. Hexagons, squares etc. The zones are contiguous
        and do not overlap.
    :cvar RING: Zones are arranged in rings . The nested inner zones are
        included in any containing  outer zones.
    :cvar ANNULAR: Zones are arranged in tiled hollow rings. The area of
        any  immediately nested zone  is excluded from the  containing
        outer zone.
    :cvar NESTED: Zones are nested, that is some zones are fully
        contained within other zones and are automatically included if
        the outer zone is selected. They may also overlap their
        neighbours.
    :cvar TILED: Zones are arranged as adjacent tiles or arbitrary
        shapes that do not overlap.
    :cvar SEQUENCE: Zones are arranged as adjacent tiles in sequence
        that touch at either or both ends. They do not overlap.
    :cvar OVERLAPPING_SEQUENCE: Zones are arranged as adjacent tiles in
        sequence that touch at either or both ends. They may partially
        overlap such that some stops are in both zones.
    :cvar OTHER:
    """
    OVERLAPPING = "overlapping"
    HONEYCOMB = "honeycomb"
    RING = "ring"
    ANNULAR = "annular"
    NESTED = "nested"
    TILED = "tiled"
    SEQUENCE = "sequence"
    OVERLAPPING_SEQUENCE = "overlappingSequence"
    OTHER = "other"
