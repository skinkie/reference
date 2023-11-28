from dataclasses import dataclass, field
from typing import List, Optional
from netex.capability_not_supported_error import CapabilityNotSupportedError
from netex.data_object_delivery import DataObjectDelivery
from netex.other_error import OtherError
from netex.producer_response_structure import ProducerResponseStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(unsafe_hash=True, kw_only=True)
class ServiceDeliveryStructure(ProducerResponseStructure):
    """
    Type for SIRI Service Delivery.

    :ivar status: Whether the complerte request could be processed
        successfully or not. Default is 'true'. If any of the individual
        requests within the delivery failed, should be set to ' false'.
    :ivar error_condition: Description of any error or warning
        conditions that appluy to the overall request. More Specific
        error conditions should be included on each request that fails.
    :ivar more_data: Whether there is a further delvery message with
        more current updates that follows this one. Default is 'false'.
    :ivar data_object_delivery:
    :ivar srs_name: Default gml coordinate format for eny location
        elements in response; applies if Coordinates element is used to
        specify points. May be overridden on individual points.
    """
    status: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    error_condition: Optional["ServiceDeliveryStructure.ErrorCondition"] = field(
        default=None,
        metadata={
            "name": "ErrorCondition",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    more_data: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MoreData",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    data_object_delivery: List[DataObjectDelivery] = field(
        default_factory=list,
        metadata={
            "name": "DataObjectDelivery",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    srs_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "srsName",
            "type": "Attribute",
        }
    )

    @dataclass(unsafe_hash=True, kw_only=True)
    class ErrorCondition:
        """
        :ivar capability_not_supported_error_or_other_error:
        :ivar description: Text description of error.
        """
        capability_not_supported_error_or_other_error: Optional[object] = field(
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
            }
        )
        description: Optional[str] = field(
            default=None,
            metadata={
                "name": "Description",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            }
        )
