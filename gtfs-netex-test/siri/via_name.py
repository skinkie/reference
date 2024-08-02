from dataclasses import dataclass

from .natural_language_place_name_structure import NaturalLanguagePlaceNameStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ViaName(NaturalLanguagePlaceNameStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
