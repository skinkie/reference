from dataclasses import dataclass

from .formation_condition_structure import FormationConditionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class FormationCondition(FormationConditionStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
