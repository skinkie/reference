from dataclasses import dataclass, field
from typing import List, Optional

from .direction_structure import DirectionStructure
from .extensions_1 import Extensions1
from .journey_pattern_ref import JourneyPatternRef
from .natural_language_string_structure import NaturalLanguageStringStructure
from .stop_point_in_pattern_structure import StopPointInPatternStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class RouteDirectionStructure(DirectionStructure):
    journey_patterns: Optional["RouteDirectionStructure.JourneyPatterns"] = field(
        default=None,
        metadata={
            "name": "JourneyPatterns",
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
    class JourneyPatterns:
        journey_pattern: List["RouteDirectionStructure.JourneyPatterns.JourneyPattern"] = field(
            default_factory=list,
            metadata={
                "name": "JourneyPattern",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )

        @dataclass(kw_only=True)
        class JourneyPattern:
            journey_pattern_ref: Optional[JourneyPatternRef] = field(
                default=None,
                metadata={
                    "name": "JourneyPatternRef",
                    "type": "Element",
                    "namespace": "http://www.siri.org.uk/siri",
                },
            )
            name: List[NaturalLanguageStringStructure] = field(
                default_factory=list,
                metadata={
                    "name": "Name",
                    "type": "Element",
                    "namespace": "http://www.siri.org.uk/siri",
                },
            )
            stops_in_pattern: Optional["RouteDirectionStructure.JourneyPatterns.JourneyPattern.StopsInPattern"] = field(
                default=None,
                metadata={
                    "name": "StopsInPattern",
                    "type": "Element",
                    "namespace": "http://www.siri.org.uk/siri",
                },
            )

            @dataclass(kw_only=True)
            class StopsInPattern:
                stop_point_in_pattern: List[StopPointInPatternStructure] = field(
                    default_factory=list,
                    metadata={
                        "name": "StopPointInPattern",
                        "type": "Element",
                        "namespace": "http://www.siri.org.uk/siri",
                        "min_occurs": 2,
                    },
                )
