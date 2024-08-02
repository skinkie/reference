from dataclasses import dataclass, field
from typing import List, Optional

from .abstract_distributor_item_structure import AbstractDistributorItemStructure
from .extensions_1 import Extensions1
from .location_structure import LocationStructure
from .natural_language_place_name_structure import NaturalLanguagePlaceNameStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class StoppingPositionChangedDepartureStructure(AbstractDistributorItemStructure):
    change_note: List[NaturalLanguagePlaceNameStructure] = field(
        default_factory=list,
        metadata={
            "name": "ChangeNote",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    new_location: Optional[LocationStructure] = field(
        default=None,
        metadata={
            "name": "NewLocation",
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
