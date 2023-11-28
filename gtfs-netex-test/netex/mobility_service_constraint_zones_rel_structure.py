from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.mobility_service_constraint_zone import MobilityServiceConstraintZone
from netex.mobility_service_constraint_zone_ref import MobilityServiceConstraintZoneRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class MobilityServiceConstraintZonesRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of references to a MOBILITY SERVICE CONSTRAINT ZONEs.
    """
    class Meta:
        name = "mobilityServiceConstraintZones_RelStructure"

    mobility_service_constraint_zone_ref_or_mobility_service_constraint_zone: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "MobilityServiceConstraintZoneRef",
                    "type": MobilityServiceConstraintZoneRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MobilityServiceConstraintZone",
                    "type": MobilityServiceConstraintZone,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
