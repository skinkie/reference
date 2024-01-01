from dataclasses import dataclass, field
from typing import Optional
from .error_code_structure import ErrorCodeStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class UnknownSubscriptionErrorStructure(ErrorCodeStructure):
    subscription_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubscriptionCode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
