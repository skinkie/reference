from dataclasses import dataclass, field
from typing import Optional

from .pushed_action_structure import PushedActionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class NotifyUserActionStructure(PushedActionStructure):
    workgroup_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "WorkgroupRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    user_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "UserName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    user_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "UserRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
