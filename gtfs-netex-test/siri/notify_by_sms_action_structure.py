from dataclasses import dataclass, field
from typing import Optional

from .pushed_action_structure import PushedActionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class NotifyBySmsActionStructure(PushedActionStructure):
    phone: Optional[str] = field(
        default=None,
        metadata={
            "name": "Phone",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    premium: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Premium",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
