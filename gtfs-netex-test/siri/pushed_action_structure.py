from dataclasses import dataclass, field
from typing import List, Optional

from xsdata.models.datatype import XmlDuration

from .parameterised_action_structure import ParameterisedActionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class PushedActionStructure(ParameterisedActionStructure):
    before_notices: Optional["PushedActionStructure.BeforeNotices"] = field(
        default=None,
        metadata={
            "name": "BeforeNotices",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    clear_notice: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ClearNotice",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )

    @dataclass(kw_only=True)
    class BeforeNotices:
        interval: List[XmlDuration] = field(
            default_factory=list,
            metadata={
                "name": "Interval",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
