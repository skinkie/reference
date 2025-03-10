from dataclasses import dataclass, field
from typing import Union

from .boarding_position import BoardingPosition
from .boarding_position_ref import BoardingPositionRef
from .containment_aggregation_structure import ContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class BoardingPositionsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "boardingPositions_RelStructure"

    boarding_position_ref_or_boarding_position: list[Union[BoardingPositionRef, BoardingPosition]] = field(
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
        },
    )
