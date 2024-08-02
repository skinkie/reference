from dataclasses import dataclass, field
from typing import Optional

from .parameterised_action_structure import ParameterisedActionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class PublishToMobileActionStructure(ParameterisedActionStructure):
    incidents: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Incidents",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    home_page: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HomePage",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
