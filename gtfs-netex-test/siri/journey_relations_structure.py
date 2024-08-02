from dataclasses import dataclass, field
from typing import List

from .journey_relation_structure import JourneyRelationStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class JourneyRelationsStructure:
    journey_relation: List[JourneyRelationStructure] = field(
        default_factory=list,
        metadata={
            "name": "JourneyRelation",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        },
    )
