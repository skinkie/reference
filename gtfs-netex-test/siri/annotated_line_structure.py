from dataclasses import dataclass, field
from typing import List, Optional

from .destination import Destination
from .extensions_1 import Extensions1
from .line_ref_structure import LineRefStructure
from .natural_language_string_structure import NaturalLanguageStringStructure
from .route_direction_structure import RouteDirectionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class AnnotatedLineStructure:
    line_ref: LineRefStructure = field(
        metadata={
            "name": "LineRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    line_name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "LineName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        },
    )
    monitored: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Monitored",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    destinations: Optional["AnnotatedLineStructure.Destinations"] = field(
        default=None,
        metadata={
            "name": "Destinations",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    directions: Optional["AnnotatedLineStructure.Directions"] = field(
        default=None,
        metadata={
            "name": "Directions",
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

    @dataclass(kw_only=True)
    class Destinations:
        destination: List[Destination] = field(
            default_factory=list,
            metadata={
                "name": "Destination",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )

    @dataclass(kw_only=True)
    class Directions:
        direction: List[RouteDirectionStructure] = field(
            default_factory=list,
            metadata={
                "name": "Direction",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )
