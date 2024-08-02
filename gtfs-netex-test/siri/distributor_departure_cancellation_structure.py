from dataclasses import dataclass, field
from typing import List, Optional

from .abstract_distributor_item_structure import AbstractDistributorItemStructure
from .extensions_1 import Extensions1
from .natural_language_string_structure import NaturalLanguageStringStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class DistributorDepartureCancellationStructure(AbstractDistributorItemStructure):
    reason: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "Reason",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    extensions: Optional[Extensions1] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
