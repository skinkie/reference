from dataclasses import dataclass

from .direction_structure import DirectionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class Direction(DirectionStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
