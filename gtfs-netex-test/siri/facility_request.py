from dataclasses import dataclass

from .facility_request_structure import FacilityRequestStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class FacilityRequest(FacilityRequestStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
