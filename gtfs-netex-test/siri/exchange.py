from dataclasses import dataclass, field
from typing import List, Optional

from xsdata.models.datatype import XmlDateTime

from .catalogue_reference import CatalogueReference
from .changed_flag_enum import ChangedFlagEnum
from .deny_reason_enum import DenyReasonEnum
from .extension_type import ExtensionType
from .filter_reference import FilterReference
from .international_identifier import InternationalIdentifier
from .request_type_enum import RequestTypeEnum
from .response_enum import ResponseEnum
from .subscription import Subscription
from .target import Target

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class Exchange:
    changed_flag: Optional[ChangedFlagEnum] = field(
        default=None,
        metadata={
            "name": "changedFlag",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    client_identification: Optional[str] = field(
        default=None,
        metadata={
            "name": "clientIdentification",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_length": 1024,
        },
    )
    delivery_break: Optional[bool] = field(
        default=None,
        metadata={
            "name": "deliveryBreak",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    deny_reason: Optional[DenyReasonEnum] = field(
        default=None,
        metadata={
            "name": "denyReason",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    historical_start_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "historicalStartDate",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    historical_stop_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "historicalStopDate",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    keep_alive: Optional[bool] = field(
        default=None,
        metadata={
            "name": "keepAlive",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    request_type: Optional[RequestTypeEnum] = field(
        default=None,
        metadata={
            "name": "requestType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    response: Optional[ResponseEnum] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    subscription_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "subscriptionReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_length": 1024,
        },
    )
    supplier_identification: InternationalIdentifier = field(
        metadata={
            "name": "supplierIdentification",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    target: Optional[Target] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    subscription: Optional[Subscription] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    filter_reference: List[FilterReference] = field(
        default_factory=list,
        metadata={
            "name": "filterReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    catalogue_reference: List[CatalogueReference] = field(
        default_factory=list,
        metadata={
            "name": "catalogueReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    exchange_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "exchangeExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
