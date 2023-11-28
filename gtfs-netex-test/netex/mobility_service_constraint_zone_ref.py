from dataclasses import dataclass
from netex.mobility_service_constraint_zone_ref_structure import MobilityServiceConstraintZoneRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class MobilityServiceConstraintZoneRef(MobilityServiceConstraintZoneRefStructure):
    """Reference to an MOBILITY SERVICE CONSTRAINT ZONE.

    +v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
