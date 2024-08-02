from dataclasses import dataclass, field
from typing import List, Union

from .abstract_subscription_request_structure import AbstractSubscriptionRequestStructure
from .connection_monitoring_subscription_request import ConnectionMonitoringSubscriptionRequest
from .connection_timetable_subscription_request import ConnectionTimetableSubscriptionRequest
from .estimated_timetable_subscription_request import EstimatedTimetableSubscriptionRequest
from .facility_monitoring_subscription_request import FacilityMonitoringSubscriptionRequest
from .general_message_subscription_request import GeneralMessageSubscriptionRequest
from .production_timetable_subscription_request import ProductionTimetableSubscriptionRequest
from .situation_exchange_subscription_request import SituationExchangeSubscriptionRequest
from .stop_monitoring_subscription_request import StopMonitoringSubscriptionRequest
from .stop_timetable_subscription_request import StopTimetableSubscriptionRequest
from .vehicle_monitoring_subscription_request import VehicleMonitoringSubscriptionRequest

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class SubscriptionRequestStructure(AbstractSubscriptionRequestStructure):
    production_timetable_subscription_request_or_estimated_timetable_subscription_request_or_stop_timetable_subscription_request_or_stop_monitoring_subscription_request_or_vehicle_monitoring_subscription_request_or_connection_timetable_subscription_request_or_connection_monitoring_subscription_request_or_general_message_subscription_request_or_facility_monitoring_subscription_request_or_situation_exchange_subscription_request: List[
        Union[
            ProductionTimetableSubscriptionRequest,
            EstimatedTimetableSubscriptionRequest,
            StopTimetableSubscriptionRequest,
            StopMonitoringSubscriptionRequest,
            VehicleMonitoringSubscriptionRequest,
            ConnectionTimetableSubscriptionRequest,
            ConnectionMonitoringSubscriptionRequest,
            GeneralMessageSubscriptionRequest,
            FacilityMonitoringSubscriptionRequest,
            SituationExchangeSubscriptionRequest,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ProductionTimetableSubscriptionRequest",
                    "type": ProductionTimetableSubscriptionRequest,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "EstimatedTimetableSubscriptionRequest",
                    "type": EstimatedTimetableSubscriptionRequest,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "StopTimetableSubscriptionRequest",
                    "type": StopTimetableSubscriptionRequest,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "StopMonitoringSubscriptionRequest",
                    "type": StopMonitoringSubscriptionRequest,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "VehicleMonitoringSubscriptionRequest",
                    "type": VehicleMonitoringSubscriptionRequest,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "ConnectionTimetableSubscriptionRequest",
                    "type": ConnectionTimetableSubscriptionRequest,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "ConnectionMonitoringSubscriptionRequest",
                    "type": ConnectionMonitoringSubscriptionRequest,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "GeneralMessageSubscriptionRequest",
                    "type": GeneralMessageSubscriptionRequest,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "FacilityMonitoringSubscriptionRequest",
                    "type": FacilityMonitoringSubscriptionRequest,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "SituationExchangeSubscriptionRequest",
                    "type": SituationExchangeSubscriptionRequest,
                    "namespace": "http://www.siri.org.uk/siri",
                },
            ),
        },
    )
