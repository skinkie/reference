from dataclasses import dataclass, field
from typing import List

from .abstract_functional_service_request_structure import AbstractFunctionalServiceRequestStructure
from .stop_monitoring_filter_structure import StopMonitoringFilterStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class StopMonitoringMultipleRequestStructure(AbstractFunctionalServiceRequestStructure):
    stop_monitoring_filter: List[StopMonitoringFilterStructure] = field(
        default_factory=list,
        metadata={
            "name": "StopMonitoringFIlter",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        },
    )
    version: str = field(
        default="2.1",
        metadata={
            "type": "Attribute",
        },
    )
