from dataclasses import dataclass, field
from typing import Optional, Union

from .capabilities_request import CapabilitiesRequest
from .capabilities_response import CapabilitiesResponse
from .check_status_request import CheckStatusRequest
from .check_status_response import CheckStatusResponse
from .connection_links_delivery import ConnectionLinksDelivery
from .connection_links_request import ConnectionLinksRequest
from .data_ready_acknowledgement import DataReadyAcknowledgement
from .data_ready_notification import DataReadyNotification
from .data_received_acknowledgement import DataReceivedAcknowledgement
from .data_supply_request import DataSupplyRequest
from .extensions_1 import Extensions1
from .facility_delivery import FacilityDelivery
from .facility_request import FacilityRequest
from .heartbeat_notification import HeartbeatNotification
from .info_channel_delivery import InfoChannelDelivery
from .info_channel_request import InfoChannelRequest
from .lines_delivery import LinesDelivery
from .lines_request import LinesRequest
from .product_categories_delivery import ProductCategoriesDelivery
from .product_categories_request import ProductCategoriesRequest
from .service_delivery import ServiceDelivery
from .service_features_delivery import ServiceFeaturesDelivery
from .service_features_request import ServiceFeaturesRequest
from .service_request import ServiceRequest
from .stop_points_delivery import StopPointsDelivery
from .stop_points_request import StopPointsRequest
from .subscription_request import SubscriptionRequest
from .subscription_response import SubscriptionResponse
from .subscription_terminated_notification import SubscriptionTerminatedNotification
from .terminate_subscription_request import TerminateSubscriptionRequest
from .terminate_subscription_response import TerminateSubscriptionResponse
from .vehicle_features_delivery import VehicleFeaturesDelivery
from .vehicle_features_request import VehicleFeaturesRequest

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class Siri:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    choice: Optional[
        Union[
            ServiceRequest,
            SubscriptionRequest,
            TerminateSubscriptionRequest,
            DataReadyNotification,
            DataSupplyRequest,
            CheckStatusRequest,
            HeartbeatNotification,
            CapabilitiesRequest,
            StopPointsRequest,
            LinesRequest,
            ServiceFeaturesRequest,
            ProductCategoriesRequest,
            VehicleFeaturesRequest,
            InfoChannelRequest,
            FacilityRequest,
            ConnectionLinksRequest,
            SubscriptionResponse,
            TerminateSubscriptionResponse,
            SubscriptionTerminatedNotification,
            DataReadyAcknowledgement,
            ServiceDelivery,
            DataReceivedAcknowledgement,
            CheckStatusResponse,
            CapabilitiesResponse,
            StopPointsDelivery,
            LinesDelivery,
            ProductCategoriesDelivery,
            ServiceFeaturesDelivery,
            VehicleFeaturesDelivery,
            InfoChannelDelivery,
            FacilityDelivery,
            ConnectionLinksDelivery,
            Extensions1,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ServiceRequest",
                    "type": ServiceRequest,
                },
                {
                    "name": "SubscriptionRequest",
                    "type": SubscriptionRequest,
                },
                {
                    "name": "TerminateSubscriptionRequest",
                    "type": TerminateSubscriptionRequest,
                },
                {
                    "name": "DataReadyNotification",
                    "type": DataReadyNotification,
                },
                {
                    "name": "DataSupplyRequest",
                    "type": DataSupplyRequest,
                },
                {
                    "name": "CheckStatusRequest",
                    "type": CheckStatusRequest,
                },
                {
                    "name": "HeartbeatNotification",
                    "type": HeartbeatNotification,
                },
                {
                    "name": "CapabilitiesRequest",
                    "type": CapabilitiesRequest,
                },
                {
                    "name": "StopPointsRequest",
                    "type": StopPointsRequest,
                },
                {
                    "name": "LinesRequest",
                    "type": LinesRequest,
                },
                {
                    "name": "ServiceFeaturesRequest",
                    "type": ServiceFeaturesRequest,
                },
                {
                    "name": "ProductCategoriesRequest",
                    "type": ProductCategoriesRequest,
                },
                {
                    "name": "VehicleFeaturesRequest",
                    "type": VehicleFeaturesRequest,
                },
                {
                    "name": "InfoChannelRequest",
                    "type": InfoChannelRequest,
                },
                {
                    "name": "FacilityRequest",
                    "type": FacilityRequest,
                },
                {
                    "name": "ConnectionLinksRequest",
                    "type": ConnectionLinksRequest,
                },
                {
                    "name": "SubscriptionResponse",
                    "type": SubscriptionResponse,
                },
                {
                    "name": "TerminateSubscriptionResponse",
                    "type": TerminateSubscriptionResponse,
                },
                {
                    "name": "SubscriptionTerminatedNotification",
                    "type": SubscriptionTerminatedNotification,
                },
                {
                    "name": "DataReadyAcknowledgement",
                    "type": DataReadyAcknowledgement,
                },
                {
                    "name": "ServiceDelivery",
                    "type": ServiceDelivery,
                },
                {
                    "name": "DataReceivedAcknowledgement",
                    "type": DataReceivedAcknowledgement,
                },
                {
                    "name": "CheckStatusResponse",
                    "type": CheckStatusResponse,
                },
                {
                    "name": "CapabilitiesResponse",
                    "type": CapabilitiesResponse,
                },
                {
                    "name": "StopPointsDelivery",
                    "type": StopPointsDelivery,
                },
                {
                    "name": "LinesDelivery",
                    "type": LinesDelivery,
                },
                {
                    "name": "ProductCategoriesDelivery",
                    "type": ProductCategoriesDelivery,
                },
                {
                    "name": "ServiceFeaturesDelivery",
                    "type": ServiceFeaturesDelivery,
                },
                {
                    "name": "VehicleFeaturesDelivery",
                    "type": VehicleFeaturesDelivery,
                },
                {
                    "name": "InfoChannelDelivery",
                    "type": InfoChannelDelivery,
                },
                {
                    "name": "FacilityDelivery",
                    "type": FacilityDelivery,
                },
                {
                    "name": "ConnectionLinksDelivery",
                    "type": ConnectionLinksDelivery,
                },
                {
                    "name": "Extensions",
                    "type": Extensions1,
                },
            ),
        },
    )
    version: str = field(
        default="2.1",
        metadata={
            "type": "Attribute",
        },
    )
