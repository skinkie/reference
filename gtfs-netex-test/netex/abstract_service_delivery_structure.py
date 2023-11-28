from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime, XmlDuration
from netex.response_structure import ResponseStructure
from netex.service_delivery_error_condition_structure import ServiceDeliveryErrorConditionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(unsafe_hash=True, kw_only=True)
class AbstractServiceDeliveryStructure(ResponseStructure):
    """
    Type for Common elementd for a SIRI service delivery of the Form xxxDelivery.

    :ivar choice:
    :ivar delegator_address: Address of original Consumer, i.e.
        requesting system to which delegating response is to be
        returned. +SIRI 2.0
    :ivar delegator_ref: Identifier of delegating system that originated
        message. +SIRI 2.0
    :ivar status:
    :ivar error_condition: Description of any error or warning
        condition.
    :ivar valid_until: End of data horizon of the data producer.
    :ivar shortest_possible_cycle: Minimum interval at which updates can
        be sent.
    :ivar default_language: Default language for text elements.
    """
    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "RequestMessageRef",
                    "type": str,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "SubscriberRef",
                    "type": str,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "SubscriptionFilterRef",
                    "type": str,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "SubscriptionRef",
                    "type": str,
                    "namespace": "http://www.siri.org.uk/siri",
                },
            ),
            "max_occurs": 3,
        }
    )
    delegator_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "DelegatorAddress",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    delegator_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "DelegatorRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    status: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    error_condition: Optional[ServiceDeliveryErrorConditionStructure] = field(
        default=None,
        metadata={
            "name": "ErrorCondition",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    valid_until: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ValidUntil",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    shortest_possible_cycle: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "ShortestPossibleCycle",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    default_language: Optional[str] = field(
        default=None,
        metadata={
            "name": "DefaultLanguage",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
