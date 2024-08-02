from dataclasses import dataclass, field
from typing import Optional

from .pushed_action_structure import PushedActionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class NotifyByPagerActionStructure(PushedActionStructure):
    pager_group_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "PagerGroupRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    pager: Optional[str] = field(
        default=None,
        metadata={
            "name": "Pager",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
