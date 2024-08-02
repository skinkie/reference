from dataclasses import dataclass, field
from typing import Optional

from .train_component_ref import TrainComponentRef
from .train_ref import TrainRef

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class PassageBetweenTrainsStructure:
    train_ref: TrainRef = field(
        metadata={
            "name": "TrainRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    train_component_ref: Optional[TrainComponentRef] = field(
        default=None,
        metadata={
            "name": "TrainComponentRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    passage_is_possible: bool = field(
        metadata={
            "name": "PassageIsPossible",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
