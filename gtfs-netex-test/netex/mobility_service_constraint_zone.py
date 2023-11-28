from dataclasses import dataclass, field
from netex.mobility_service_constraint_zone_version_structure import MobilityServiceConstraintZoneVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class MobilityServiceConstraintZone(MobilityServiceConstraintZoneVersionStructure):
    """
    ZONE defining a restriction on used of a MOBILITY SERVICE, e.g. no entry, no
    drop off, etc, etc   +v1.2.2.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
