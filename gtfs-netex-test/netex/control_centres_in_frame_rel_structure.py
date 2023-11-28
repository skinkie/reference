from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.control_centre import ControlCentre

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ControlCentresInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of CONTROL CENTREs.

    :ivar control_centre: Characterization of a set of operational
        objects, such as timing or links determined either by a
        DEPARTMENT or by an ORGANISATIONAL UNIT.
    """
    class Meta:
        name = "controlCentresInFrame_RelStructure"

    control_centre: List[ControlCentre] = field(
        default_factory=list,
        metadata={
            "name": "ControlCentre",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
