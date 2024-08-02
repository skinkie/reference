from dataclasses import dataclass

from .facility_condition_structure import FacilityConditionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class FacilityConditionElement(FacilityConditionStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
