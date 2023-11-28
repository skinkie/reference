from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.mobility_service_constraint_zone import MobilityServiceConstraintZone

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class MobilityServiceConstraintZonesInFrameRelStructure(ContainmentAggregationStructure):
    """Type for a list of references to a MOBILITY SERVICE CONSTRAINT ZONEs.

    in Frame
    """
    class Meta:
        name = "mobilityServiceConstraintZonesInFrame_RelStructure"

    mobility_service_constraint_zone: List[MobilityServiceConstraintZone] = field(
        default_factory=list,
        metadata={
            "name": "MobilityServiceConstraintZone",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
