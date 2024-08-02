from dataclasses import dataclass, field
from typing import Optional

from .parameterised_action_structure import ParameterisedActionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class PublishToTvActionStructure(ParameterisedActionStructure):
    ceefax: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Ceefax",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    teletext: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Teletext",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
