from dataclasses import dataclass, field
from typing import List

from .natural_language_string_structure import NaturalLanguageStringStructure
from .train_part_ref_structure import TrainPartRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class TrainBlockPartStructure:
    number_of_block_parts: int = field(
        metadata={
            "name": "NumberOfBlockParts",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    train_part_ref: TrainPartRefStructure = field(
        metadata={
            "name": "TrainPartRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    position_of_train_block_part: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "PositionOfTrainBlockPart",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
