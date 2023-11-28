from dataclasses import dataclass, field
from typing import Optional
from netex.consumer_response_endpoint_structure import ConsumerResponseEndpointStructure
from netex.other_error import OtherError
from netex.unknown_subscription_error import UnknownSubscriptionError

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(unsafe_hash=True, kw_only=True)
class DataReadyResponseStructure(ConsumerResponseEndpointStructure):
    """
    Type for Data ready Acknowledgement Response.

    :ivar status:
    :ivar error_condition: Description of any error or warning condition
        as to why Consumer cannot fetch data.
    """
    status: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    error_condition: Optional["DataReadyResponseStructure.ErrorCondition"] = field(
        default=None,
        metadata={
            "name": "ErrorCondition",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )

    @dataclass(unsafe_hash=True, kw_only=True)
    class ErrorCondition:
        """
        :ivar unknown_subscription_error_or_other_error:
        :ivar description: Text description of error.
        """
        unknown_subscription_error_or_other_error: Optional[object] = field(
            default=None,
            metadata={
                "type": "Elements",
                "choices": (
                    {
                        "name": "UnknownSubscriptionError",
                        "type": UnknownSubscriptionError,
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
