from dataclasses import dataclass, field
from typing import List
from netex.frame_containment_structure import FrameContainmentStructure
from netex.series_constraint import SeriesConstraint

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FareSeriesInFrameRelStructure(FrameContainmentStructure):
    """
    Type for containment in frame of SERIES CONSTRAINT.
    """
    class Meta:
        name = "fareSeriesInFrame_RelStructure"

    series_constraint: List[SeriesConstraint] = field(
        default_factory=list,
        metadata={
            "name": "SeriesConstraint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
