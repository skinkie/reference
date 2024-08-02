from dataclasses import dataclass, field
from typing import List

from .related_situation_structure import RelatedSituationStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ReferencesStructure:
    related_to_ref: List[RelatedSituationStructure] = field(
        default_factory=list,
        metadata={
            "name": "RelatedToRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        },
    )
