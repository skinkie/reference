from dataclasses import dataclass

from .situation_ref_structure import SituationRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class SituationRef(SituationRefStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
