from dataclasses import dataclass, field
from typing import List

from .frame_containment_structure import FrameContainmentStructure
from .series_constraint import SeriesConstraint

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareSeriesInFrameRelStructure(FrameContainmentStructure):
    class Meta:
        name = "fareSeriesInFrame_RelStructure"

    series_constraint: List[SeriesConstraint] = field(
        default_factory=list,
        metadata={
            "name": "SeriesConstraint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
