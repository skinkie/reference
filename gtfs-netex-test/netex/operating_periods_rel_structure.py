from dataclasses import dataclass, field
from typing import Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .operating_period import OperatingPeriod
from .operating_period_ref import OperatingPeriodRef
from .uic_operating_period import UicOperatingPeriod
from .uic_operating_period_ref import UicOperatingPeriodRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class OperatingPeriodsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "operatingPeriods_RelStructure"

    uic_operating_period_ref_or_operating_period_ref_or_operating_period_or_uic_operating_period: list[Union[UicOperatingPeriodRef, OperatingPeriodRef, OperatingPeriod, UicOperatingPeriod]] = field(
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
        },
    )
