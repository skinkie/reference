from dataclasses import dataclass

from .natural_language_string_structure import NaturalLanguageStringStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class VehicleOrientationRelativeToQuay(NaturalLanguageStringStructure):
    pass
