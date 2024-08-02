from dataclasses import dataclass, field
from typing import List, Optional

from .action_data_structure import ActionDataStructure
from .closed_timestamp_range_structure import ClosedTimestampRangeStructure
from .natural_language_string_structure import NaturalLanguageStringStructure
from .simple_action_structure import SimpleActionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ParameterisedActionStructure(SimpleActionStructure):
    description: Optional[NaturalLanguageStringStructure] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    action_data: List[ActionDataStructure] = field(
        default_factory=list,
        metadata={
            "name": "ActionData",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    publication_window: List[ClosedTimestampRangeStructure] = field(
        default_factory=list,
        metadata={
            "name": "PublicationWindow",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
