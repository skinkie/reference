from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.operational_context import OperationalContext

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class OperationalContextsInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of OPERATIONAL CONTEXTs.

    :ivar operational_context: Characterization of a set of operational
        objects, such as timing or links determined either by a
        DEPARTMENT or by an ORGANISATIONAL UNIT.
    """
    class Meta:
        name = "operationalContextsInFrame_RelStructure"

    operational_context: List[OperationalContext] = field(
        default_factory=list,
        metadata={
            "name": "OperationalContext",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
