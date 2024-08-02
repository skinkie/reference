from dataclasses import dataclass

from .journey_place_ref_structure import JourneyPlaceRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ViaRef(JourneyPlaceRefStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
