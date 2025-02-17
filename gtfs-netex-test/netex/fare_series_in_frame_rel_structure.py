from dataclasses import dataclass, field

from .frame_containment_structure import FrameContainmentStructure
from .series_constraint import SeriesConstraint

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class FareSeriesInFrameRelStructure(FrameContainmentStructure):
    class Meta:
        name = "fareSeriesInFrame_RelStructure"

    series_constraint: list[SeriesConstraint] = field(
        default_factory=list,
        metadata={
            "name": "SeriesConstraint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
