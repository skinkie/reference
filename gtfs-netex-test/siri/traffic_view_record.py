from dataclasses import dataclass, field
from typing import List, Optional

from .elaborated_data import ElaboratedData
from .extension_type import ExtensionType
from .operator_action import OperatorAction
from .traffic_element import TrafficElement
from .url_link import UrlLink

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class TrafficViewRecord:
    record_sequence_number: int = field(
        metadata={
            "name": "recordSequenceNumber",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    traffic_element: Optional[TrafficElement] = field(
        default=None,
        metadata={
            "name": "trafficElement",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    operator_action: Optional[OperatorAction] = field(
        default=None,
        metadata={
            "name": "operatorAction",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    elaborated_data: Optional[ElaboratedData] = field(
        default=None,
        metadata={
            "name": "elaboratedData",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    url_link: List[UrlLink] = field(
        default_factory=list,
        metadata={
            "name": "urlLink",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    traffic_view_record_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "trafficViewRecordExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
