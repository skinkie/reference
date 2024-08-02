from dataclasses import dataclass, field
from typing import List, Optional

from .abstract_service_delivery_structure import AbstractServiceDeliveryStructure
from .extensions_1 import Extensions1
from .monitored_stop_visit import MonitoredStopVisit
from .monitored_stop_visit_cancellation import MonitoredStopVisitCancellation
from .monitoring_ref_structure import MonitoringRefStructure
from .natural_language_string_structure import NaturalLanguageStringStructure
from .service_exception import ServiceException
from .stop_line_notice import StopLineNotice
from .stop_line_notice_cancellation import StopLineNoticeCancellation
from .stop_notice import StopNotice
from .stop_notice_cancellation import StopNoticeCancellation

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class StopMonitoringDeliveryStructure(AbstractServiceDeliveryStructure):
    monitoring_ref: List[MonitoringRefStructure] = field(
        default_factory=list,
        metadata={
            "name": "MonitoringRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    monitoring_name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "MonitoringName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    monitored_stop_visit: List[MonitoredStopVisit] = field(
        default_factory=list,
        metadata={
            "name": "MonitoredStopVisit",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    monitored_stop_visit_cancellation: List[MonitoredStopVisitCancellation] = field(
        default_factory=list,
        metadata={
            "name": "MonitoredStopVisitCancellation",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_line_notice: List[StopLineNotice] = field(
        default_factory=list,
        metadata={
            "name": "StopLineNotice",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_line_notice_cancellation: List[StopLineNoticeCancellation] = field(
        default_factory=list,
        metadata={
            "name": "StopLineNoticeCancellation",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_notice: List[StopNotice] = field(
        default_factory=list,
        metadata={
            "name": "StopNotice",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_notice_cancellation: List[StopNoticeCancellation] = field(
        default_factory=list,
        metadata={
            "name": "StopNoticeCancellation",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    service_exception: List[ServiceException] = field(
        default_factory=list,
        metadata={
            "name": "ServiceException",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    note: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "Note",
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
