from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .mobility_service_constraint_zone import MobilityServiceConstraintZone

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class MobilityServiceConstraintZonesInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "mobilityServiceConstraintZonesInFrame_RelStructure"

    mobility_service_constraint_zone: list[MobilityServiceConstraintZone] = field(
        default_factory=list,
        metadata={
            "name": "MobilityServiceConstraintZone",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
