from dataclasses import dataclass, field
from typing import List, Optional

from .abstract_service_delivery_structure import AbstractServiceDeliveryStructure
from .extensions_1 import Extensions1
from .facility_condition import FacilityCondition

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class FacilityMonitoringDeliveryStructure(AbstractServiceDeliveryStructure):
    facility_condition: List[FacilityCondition] = field(
        default_factory=list,
        metadata={
            "name": "FacilityCondition",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    extensions: Optional[Extensions1] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    version: str = field(
        default="2.1",
        metadata={
            "type": "Attribute",
        },
    )
