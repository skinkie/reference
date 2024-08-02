from dataclasses import dataclass, field
from typing import Optional

from .parameterised_action_structure import ParameterisedActionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class PublishToDisplayActionStructure(ParameterisedActionStructure):
    on_place: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OnPlace",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    on_board: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OnBoard",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
