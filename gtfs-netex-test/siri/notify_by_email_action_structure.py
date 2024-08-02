from dataclasses import dataclass, field
from typing import Optional

from .pushed_action_structure import PushedActionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class NotifyByEmailActionStructure(PushedActionStructure):
    email: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
