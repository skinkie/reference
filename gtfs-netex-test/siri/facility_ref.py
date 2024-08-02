from dataclasses import dataclass

from .facility_ref_structure import FacilityRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class FacilityRef(FacilityRefStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
