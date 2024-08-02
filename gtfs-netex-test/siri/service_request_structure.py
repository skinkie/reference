from dataclasses import dataclass, field
from typing import List, Union

from .connection_monitoring_request import ConnectionMonitoringRequest
from .connection_timetable_request import ConnectionTimetableRequest
from .contextualised_request_structure import ContextualisedRequestStructure
from .estimated_timetable_request import EstimatedTimetableRequest
from .facility_monitoring_request import FacilityMonitoringRequest
from .general_message_request import GeneralMessageRequest
from .production_timetable_request import ProductionTimetableRequest
from .situation_exchange_request import SituationExchangeRequest
from .stop_monitoring_multiple_request import StopMonitoringMultipleRequest
from .stop_monitoring_request import StopMonitoringRequest
from .stop_timetable_request import StopTimetableRequest
from .vehicle_monitoring_request import VehicleMonitoringRequest

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ServiceRequestStructure(ContextualisedRequestStructure):
    choice: List[Union[ProductionTimetableRequest, EstimatedTimetableRequest, StopTimetableRequest, StopMonitoringMultipleRequest, StopMonitoringRequest, VehicleMonitoringRequest, ConnectionTimetableRequest, ConnectionMonitoringRequest, GeneralMessageRequest, FacilityMonitoringRequest, SituationExchangeRequest]] = (
        field(
            default_factory=list,
            metadata={
                "type": "Elements",
                "choices": (
                    {
                        "name": "ProductionTimetableRequest",
                        "type": ProductionTimetableRequest,
                        "namespace": "http://www.siri.org.uk/siri",
                    },
                    {
                        "name": "EstimatedTimetableRequest",
                        "type": EstimatedTimetableRequest,
                        "namespace": "http://www.siri.org.uk/siri",
                    },
                    {
                        "name": "StopTimetableRequest",
                        "type": StopTimetableRequest,
                        "namespace": "http://www.siri.org.uk/siri",
                    },
                    {
                        "name": "StopMonitoringMultipleRequest",
                        "type": StopMonitoringMultipleRequest,
                        "namespace": "http://www.siri.org.uk/siri",
                    },
                    {
                        "name": "StopMonitoringRequest",
                        "type": StopMonitoringRequest,
                        "namespace": "http://www.siri.org.uk/siri",
                    },
                    {
                        "name": "VehicleMonitoringRequest",
                        "type": VehicleMonitoringRequest,
                        "namespace": "http://www.siri.org.uk/siri",
                    },
                    {
                        "name": "ConnectionTimetableRequest",
                        "type": ConnectionTimetableRequest,
                        "namespace": "http://www.siri.org.uk/siri",
                    },
                    {
                        "name": "ConnectionMonitoringRequest",
                        "type": ConnectionMonitoringRequest,
                        "namespace": "http://www.siri.org.uk/siri",
                    },
                    {
                        "name": "GeneralMessageRequest",
                        "type": GeneralMessageRequest,
                        "namespace": "http://www.siri.org.uk/siri",
                    },
                    {
                        "name": "FacilityMonitoringRequest",
                        "type": FacilityMonitoringRequest,
                        "namespace": "http://www.siri.org.uk/siri",
                    },
                    {
                        "name": "SituationExchangeRequest",
                        "type": SituationExchangeRequest,
                        "namespace": "http://www.siri.org.uk/siri",
                    },
                ),
            },
        )
    )
