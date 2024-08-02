from dataclasses import dataclass, field
from typing import Optional

from .authenticated_request_structure import AuthenticatedRequestStructure
from .connection_monitoring_capabilities_request import ConnectionMonitoringCapabilitiesRequest
from .connection_timetable_capabilities_request import ConnectionTimetableCapabilitiesRequest
from .estimated_timetable_capabilities_request import EstimatedTimetableCapabilitiesRequest
from .facility_monitoring_capabilities_request import FacilityMonitoringCapabilitiesRequest
from .general_message_capabilities_request import GeneralMessageCapabilitiesRequest
from .participant_ref_structure import ParticipantRefStructure
from .production_timetable_capabilities_request import ProductionTimetableCapabilitiesRequest
from .requestor_ref import RequestorRef
from .situation_exchange_capabilities_request import SituationExchangeCapabilitiesRequest
from .stop_monitoring_capabilities_request import StopMonitoringCapabilitiesRequest
from .stop_timetable_capabilities_request import StopTimetableCapabilitiesRequest
from .vehicle_monitoring_capabilities_request import VehicleMonitoringCapabilitiesRequest

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class CapabilitiesRequestStructure(AuthenticatedRequestStructure):
    address: Optional[str] = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    requestor_ref: RequestorRef = field(
        metadata={
            "name": "RequestorRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    delegator_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "DelegatorAddress",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    delegator_ref: Optional[ParticipantRefStructure] = field(
        default=None,
        metadata={
            "name": "DelegatorRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    production_timetable_capabilities_request: Optional[ProductionTimetableCapabilitiesRequest] = field(
        default=None,
        metadata={
            "name": "ProductionTimetableCapabilitiesRequest",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    estimated_timetable_capabilities_request: Optional[EstimatedTimetableCapabilitiesRequest] = field(
        default=None,
        metadata={
            "name": "EstimatedTimetableCapabilitiesRequest",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_timetable_capabilities_request: Optional[StopTimetableCapabilitiesRequest] = field(
        default=None,
        metadata={
            "name": "StopTimetableCapabilitiesRequest",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_monitoring_capabilities_request: Optional[StopMonitoringCapabilitiesRequest] = field(
        default=None,
        metadata={
            "name": "StopMonitoringCapabilitiesRequest",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    vehicle_monitoring_capabilities_request: Optional[VehicleMonitoringCapabilitiesRequest] = field(
        default=None,
        metadata={
            "name": "VehicleMonitoringCapabilitiesRequest",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    connection_timetable_capabilities_request: Optional[ConnectionTimetableCapabilitiesRequest] = field(
        default=None,
        metadata={
            "name": "ConnectionTimetableCapabilitiesRequest",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    connection_monitoring_capabilities_request: Optional[ConnectionMonitoringCapabilitiesRequest] = field(
        default=None,
        metadata={
            "name": "ConnectionMonitoringCapabilitiesRequest",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    general_message_capabilities_request: Optional[GeneralMessageCapabilitiesRequest] = field(
        default=None,
        metadata={
            "name": "GeneralMessageCapabilitiesRequest",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    facility_monitoring_capabilities_request: Optional[FacilityMonitoringCapabilitiesRequest] = field(
        default=None,
        metadata={
            "name": "FacilityMonitoringCapabilitiesRequest",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    situation_exchange_capabilities_request: Optional[SituationExchangeCapabilitiesRequest] = field(
        default=None,
        metadata={
            "name": "SituationExchangeCapabilitiesRequest",
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
