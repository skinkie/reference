from dataclasses import dataclass

from .situation_full_ref_structure import SituationFullRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class SituationFullRef(SituationFullRefStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
