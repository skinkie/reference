from dataclasses import dataclass

from .pt_situation_element_structure import PtSituationElementStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class PtSituationElement(PtSituationElementStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
