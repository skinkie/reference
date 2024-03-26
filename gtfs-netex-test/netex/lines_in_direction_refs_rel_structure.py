from dataclasses import dataclass, field
from typing import List, Union

from .allowed_line_direction_ref import AllowedLineDirectionRef
from .containment_aggregation_structure import ContainmentAggregationStructure
from .line_in_direction_ref import LineInDirectionRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LinesInDirectionRefsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "linesInDirectionRefs_RelStructure"

    line_in_direction_ref_or_allowed_line_direction_ref: List[
        Union[LineInDirectionRef, AllowedLineDirectionRef]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "LineInDirectionRef",
                    "type": LineInDirectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AllowedLineDirectionRef",
                    "type": AllowedLineDirectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
