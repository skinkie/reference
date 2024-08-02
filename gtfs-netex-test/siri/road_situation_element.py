from dataclasses import dataclass

from .road_situation_element_structure import RoadSituationElementStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class RoadSituationElement(RoadSituationElementStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
