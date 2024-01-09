from dataclasses import dataclass, field
from typing import Optional, Union
from .anschluss_plan_type import AnschlussPlanType
from .anschluss_status_type import AnschlussStatusType


@dataclass(kw_only=True)
class GesAnschlussType:
    anschluss_plan_or_anschluss_status: Optional[
        Union[AnschlussPlanType, AnschlussStatusType]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AnschlussPlan",
                    "type": AnschlussPlanType,
                    "namespace": "",
                },
                {
                    "name": "AnschlussStatus",
                    "type": AnschlussStatusType,
                    "namespace": "",
                },
            ),
        },
    )
