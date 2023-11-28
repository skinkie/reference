from dataclasses import dataclass
from netex.zone_ref_structure import ZoneRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class MobilityServiceConstraintZoneRefStructure(ZoneRefStructure):
    """Type for Reference to an MOBILITY SERVICE CONSTRAINT ZONE.

    Left untyped so as to avoid forwards dependency.
    """
