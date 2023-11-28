from dataclasses import dataclass, field
from typing import Optional
from netex.error_code_structure import ErrorCodeStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(unsafe_hash=True, kw_only=True)
class UnknownSubscriptionErrorStructure(ErrorCodeStructure):
    """Type for Error: Subscription not found.

    :ivar subscription_code: Ubscription code that could not be found. +
        SIRI v2.0
    """
    subscription_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubscriptionCode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
