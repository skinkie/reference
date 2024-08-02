from dataclasses import dataclass

from .facility_change_structure import FacilityChangeStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class FacilityChangeElement(FacilityChangeStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
