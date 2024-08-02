from dataclasses import dataclass, field
from typing import ForwardRef, Optional, Union

from xsdata.models.datatype import XmlDuration

from .abstract_subscription_structure import AbstractSubscriptionStructure
from .extensions_1 import Extensions1
from .vehicle_monitoring_request import VehicleMonitoringRequest

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class VehicleMonitoringSubscriptionStructure(AbstractSubscriptionStructure):
    vehicle_monitoring_request: VehicleMonitoringRequest = field(
        metadata={
            "name": "VehicleMonitoringRequest",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    incremental_updates: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IncrementalUpdates",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    change_before_updates_or_update_interval: Optional[Union["VehicleMonitoringSubscriptionStructure.ChangeBeforeUpdates", "VehicleMonitoringSubscriptionStructure.UpdateInterval"]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ChangeBeforeUpdates",
                    "type": ForwardRef("VehicleMonitoringSubscriptionStructure.ChangeBeforeUpdates"),
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "UpdateInterval",
                    "type": ForwardRef("VehicleMonitoringSubscriptionStructure.UpdateInterval"),
                    "namespace": "http://www.siri.org.uk/siri",
                },
            ),
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

    @dataclass(kw_only=True)
    class ChangeBeforeUpdates:
        value: XmlDuration = field(
            metadata={
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class UpdateInterval:
        value: XmlDuration = field(
            metadata={
                "required": True,
            }
        )
