from dataclasses import dataclass, field
from typing import List, Union

from .connection_monitoring_distributor_delivery import ConnectionMonitoringDistributorDelivery
from .connection_monitoring_feeder_delivery import ConnectionMonitoringFeederDelivery
from .connection_timetable_delivery import ConnectionTimetableDelivery
from .estimated_timetable_delivery import EstimatedTimetableDelivery
from .facility_monitoring_delivery import FacilityMonitoringDelivery
from .general_message_delivery import GeneralMessageDelivery
from .included_situation_exchange_delivery import IncludedSituationExchangeDelivery
from .production_timetable_delivery import ProductionTimetableDelivery
from .situation_exchange_delivery import SituationExchangeDelivery
from .stop_monitoring_delivery import StopMonitoringDelivery
from .stop_timetable_delivery import StopTimetableDelivery
from .vehicle_monitoring_delivery import VehicleMonitoringDelivery

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class SiriServiceDeliveryStructure:
    choice: List[
        Union[
            IncludedSituationExchangeDelivery,
            ProductionTimetableDelivery,
            EstimatedTimetableDelivery,
            StopTimetableDelivery,
            StopMonitoringDelivery,
            VehicleMonitoringDelivery,
            ConnectionTimetableDelivery,
            ConnectionMonitoringFeederDelivery,
            ConnectionMonitoringDistributorDelivery,
            GeneralMessageDelivery,
            FacilityMonitoringDelivery,
            SituationExchangeDelivery,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "IncludedSituationExchangeDelivery",
                    "type": IncludedSituationExchangeDelivery,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "ProductionTimetableDelivery",
                    "type": ProductionTimetableDelivery,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "EstimatedTimetableDelivery",
                    "type": EstimatedTimetableDelivery,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "StopTimetableDelivery",
                    "type": StopTimetableDelivery,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "StopMonitoringDelivery",
                    "type": StopMonitoringDelivery,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "VehicleMonitoringDelivery",
                    "type": VehicleMonitoringDelivery,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "ConnectionTimetableDelivery",
                    "type": ConnectionTimetableDelivery,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "ConnectionMonitoringFeederDelivery",
                    "type": ConnectionMonitoringFeederDelivery,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "ConnectionMonitoringDistributorDelivery",
                    "type": ConnectionMonitoringDistributorDelivery,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "GeneralMessageDelivery",
                    "type": GeneralMessageDelivery,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "FacilityMonitoringDelivery",
                    "type": FacilityMonitoringDelivery,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "SituationExchangeDelivery",
                    "type": SituationExchangeDelivery,
                    "namespace": "http://www.siri.org.uk/siri",
                },
            ),
        },
    )
