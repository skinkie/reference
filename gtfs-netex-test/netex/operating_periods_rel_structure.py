from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.operating_period import OperatingPeriod
from netex.operating_period_ref import OperatingPeriodRef
from netex.uic_operating_period import UicOperatingPeriod
from netex.uic_operating_period_ref import UicOperatingPeriodRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class OperatingPeriodsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of OPERATING PERIODs.
    """
    class Meta:
        name = "operatingPeriods_RelStructure"

    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "UicOperatingPeriodRef",
                    "type": UicOperatingPeriodRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OperatingPeriodRef",
                    "type": OperatingPeriodRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
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
