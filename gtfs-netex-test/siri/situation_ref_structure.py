from dataclasses import dataclass, field
from typing import Optional

from .situation_full_ref import SituationFullRef
from .situation_simple_ref import SituationSimpleRef

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class SituationRefStructure:
    situation_simple_ref: Optional[SituationSimpleRef] = field(
        default=None,
        metadata={
            "name": "SituationSimpleRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    situation_full_ref: Optional[SituationFullRef] = field(
        default=None,
        metadata={
            "name": "SituationFullRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
