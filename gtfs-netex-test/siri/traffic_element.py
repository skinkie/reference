from dataclasses import dataclass, field
from typing import Optional

from .extension_type import ExtensionType
from .situation_record import SituationRecord

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class TrafficElement(SituationRecord):
    traffic_element_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "trafficElementExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
