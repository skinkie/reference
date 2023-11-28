from dataclasses import dataclass, field
from typing import List
from netex.allowed_line_direction import AllowedLineDirection
from netex.allowed_line_direction_ref import AllowedLineDirectionRef
from netex.containment_aggregation_structure import ContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AllowedLineDirectionsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of ALLOWED LINE DIRECTIONs.
    """
    class Meta:
        name = "allowedLineDirections_RelStructure"

    allowed_line_direction_ref_or_allowed_line_direction: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AllowedLineDirectionRef",
                    "type": AllowedLineDirectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AllowedLineDirection",
                    "type": AllowedLineDirection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
