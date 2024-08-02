from dataclasses import dataclass, field
from typing import Optional

from .pushed_action_structure import PushedActionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class PublishToAlertsActionStructure(PushedActionStructure):
    by_email: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ByEmail",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    by_mobile: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ByMobile",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
