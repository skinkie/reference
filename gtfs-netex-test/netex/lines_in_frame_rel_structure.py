from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.flexible_line import FlexibleLine
from netex.line import Line

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class LinesInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of LINe.
    """
    class Meta:
        name = "linesInFrame_RelStructure"

    flexible_line_or_line: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FlexibleLine",
                    "type": FlexibleLine,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Line",
                    "type": Line,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
