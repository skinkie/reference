from dataclasses import dataclass, field
from typing import List
from netex.boarding_position import BoardingPosition
from netex.boarding_position_ref import BoardingPositionRef
from netex.containment_aggregation_structure import ContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class BoardingPositionsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of BOARDING POSITIONs.
    """
    class Meta:
        name = "boardingPositions_RelStructure"

    boarding_position_ref_or_boarding_position: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "BoardingPositionRef",
                    "type": BoardingPositionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BoardingPosition",
                    "type": BoardingPosition,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
