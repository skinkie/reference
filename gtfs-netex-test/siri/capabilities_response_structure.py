from dataclasses import dataclass, field
from typing import Optional

from .connection_monitoring_capabilities_response import ConnectionMonitoringCapabilitiesResponse
from .connection_timetable_capabilities_response import ConnectionTimetableCapabilitiesResponse
from .estimated_timetable_capabilities_response import EstimatedTimetableCapabilitiesResponse
from .facility_monitoring_capabilities_response import FacilityMonitoringCapabilitiesResponse
from .general_message_capabilities_response import GeneralMessageCapabilitiesResponse
from .producer_response_structure import ProducerResponseStructure
from .production_timetable_capabilities_response import ProductionTimetableCapabilitiesResponse
from .situation_exchange_capabilities_response import SituationExchangeCapabilitiesResponse
from .stop_monitoring_capabilities_response import StopMonitoringCapabilitiesResponse
from .stop_timetable_capabilities_response import StopTimetableCapabilitiesResponse
from .vehicle_monitoring_capabilities_response import VehicleMonitoringCapabilitiesResponse

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class CapabilitiesResponseStructure(ProducerResponseStructure):
    production_timetable_capabilities_response: Optional[ProductionTimetableCapabilitiesResponse] = field(
        default=None,
        metadata={
            "name": "ProductionTimetableCapabilitiesResponse",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    estimated_timetable_capabilities_response: Optional[EstimatedTimetableCapabilitiesResponse] = field(
        default=None,
        metadata={
            "name": "EstimatedTimetableCapabilitiesResponse",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_timetable_capabilities_response: Optional[StopTimetableCapabilitiesResponse] = field(
        default=None,
        metadata={
            "name": "StopTimetableCapabilitiesResponse",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_monitoring_capabilities_response: Optional[StopMonitoringCapabilitiesResponse] = field(
        default=None,
        metadata={
            "name": "StopMonitoringCapabilitiesResponse",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    vehicle_monitoring_capabilities_response: Optional[VehicleMonitoringCapabilitiesResponse] = field(
        default=None,
        metadata={
            "name": "VehicleMonitoringCapabilitiesResponse",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    connection_timetable_capabilities_response: Optional[ConnectionTimetableCapabilitiesResponse] = field(
        default=None,
        metadata={
            "name": "ConnectionTimetableCapabilitiesResponse",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    connection_monitoring_capabilities_response: Optional[ConnectionMonitoringCapabilitiesResponse] = field(
        default=None,
        metadata={
            "name": "ConnectionMonitoringCapabilitiesResponse",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    general_message_capabilities_response: Optional[GeneralMessageCapabilitiesResponse] = field(
        default=None,
        metadata={
            "name": "GeneralMessageCapabilitiesResponse",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    facility_monitoring_capabilities_response: Optional[FacilityMonitoringCapabilitiesResponse] = field(
        default=None,
        metadata={
            "name": "FacilityMonitoringCapabilitiesResponse",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    situation_exchange_capabilities_response: Optional[SituationExchangeCapabilitiesResponse] = field(
        default=None,
        metadata={
            "name": "SituationExchangeCapabilitiesResponse",
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
