from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.operating_period import OperatingPeriod
from netex.uic_operating_period import UicOperatingPeriod

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class OperatingPeriodsInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of OPERATING PERIODs.
    """
    class Meta:
        name = "operatingPeriodsInFrame_RelStructure"

    operating_period_or_uic_operating_period: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "OperatingPeriod",
                    "type": OperatingPeriod,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UicOperatingPeriod",
                    "type": UicOperatingPeriod,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
