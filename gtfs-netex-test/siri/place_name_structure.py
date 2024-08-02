from dataclasses import dataclass, field
from typing import List, Optional

from .journey_place_ref_structure import JourneyPlaceRefStructure
from .natural_language_place_name_structure import NaturalLanguagePlaceNameStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class PlaceNameStructure:
    place_ref: Optional[JourneyPlaceRefStructure] = field(
        default=None,
        metadata={
            "name": "PlaceRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    place_name: List[NaturalLanguagePlaceNameStructure] = field(
        default_factory=list,
        metadata={
            "name": "PlaceName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    place_short_name: List[NaturalLanguagePlaceNameStructure] = field(
        default_factory=list,
        metadata={
            "name": "PlaceShortName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
