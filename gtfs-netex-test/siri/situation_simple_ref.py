from dataclasses import dataclass

from .situation_simple_ref_structure import SituationSimpleRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class SituationSimpleRef(SituationSimpleRefStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
