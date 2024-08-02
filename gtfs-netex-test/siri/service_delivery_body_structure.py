from dataclasses import dataclass, field
from typing import List, Optional, Union

from .capability_not_supported_error import CapabilityNotSupportedError
from .connection_monitoring_distributor_delivery import ConnectionMonitoringDistributorDelivery
from .connection_monitoring_feeder_delivery import ConnectionMonitoringFeederDelivery
from .connection_timetable_delivery import ConnectionTimetableDelivery
from .error_description_structure import ErrorDescriptionStructure
from .estimated_timetable_delivery import EstimatedTimetableDelivery
from .facility_monitoring_delivery import FacilityMonitoringDelivery
from .general_message_delivery import GeneralMessageDelivery
from .included_situation_exchange_delivery import IncludedSituationExchangeDelivery
from .other_error import OtherError
from .production_timetable_delivery import ProductionTimetableDelivery
from .situation_exchange_delivery import SituationExchangeDelivery
from .stop_monitoring_delivery import StopMonitoringDelivery
from .stop_timetable_delivery import StopTimetableDelivery
from .vehicle_monitoring_delivery import VehicleMonitoringDelivery

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ServiceDeliveryBodyStructure:
    status: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    error_condition: Optional["ServiceDeliveryBodyStructure.ErrorCondition"] = field(
        default=None,
        metadata={
            "name": "ErrorCondition",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    more_data: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MoreData",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
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
    srs_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "srsName",
            "type": "Attribute",
        },
    )

    @dataclass(kw_only=True)
    class ErrorCondition:
        capability_not_supported_error_or_other_error: Optional[Union[CapabilityNotSupportedError, OtherError]] = field(
            default=None,
            metadata={
                "type": "Elements",
                "choices": (
                    {
                        "name": "CapabilityNotSupportedError",
                        "type": CapabilityNotSupportedError,
                        "namespace": "http://www.siri.org.uk/siri",
                    },
                    {
                        "name": "OtherError",
                        "type": OtherError,
                        "namespace": "http://www.siri.org.uk/siri",
                    },
                ),
            },
        )
        description: Optional[ErrorDescriptionStructure] = field(
            default=None,
            metadata={
                "name": "Description",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
