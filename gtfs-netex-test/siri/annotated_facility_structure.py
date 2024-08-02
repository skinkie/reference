from dataclasses import dataclass, field
from typing import Optional

from .facility_ref import FacilityRef
from .facility_structure import FacilityStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class AnnotatedFacilityStructure:
    facility_ref: FacilityRef = field(
        metadata={
            "name": "FacilityRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    monitored: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Monitored",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    facility: Optional[FacilityStructure] = field(
        default=None,
        metadata={
            "name": "Facility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
