from dataclasses import dataclass, field
from typing import List, Optional

from .extensions_1 import Extensions1
from .facility_ref import FacilityRef
from .facility_status_enumeration import FacilityStatusEnumeration
from .natural_language_string_structure import NaturalLanguageStringStructure
from .stop_point_ref_structure import StopPointRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class AffectedFacilityStructure:
    facility_ref: Optional[FacilityRef] = field(
        default=None,
        metadata={
            "name": "FacilityRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    start_stop_point_ref: Optional[StopPointRefStructure] = field(
        default=None,
        metadata={
            "name": "StartStopPointRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    end_stop_point_ref: Optional[StopPointRefStructure] = field(
        default=None,
        metadata={
            "name": "EndStopPointRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    facility_name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "FacilityName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    facility_status: List[FacilityStatusEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "FacilityStatus",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    extensions: List[Extensions1] = field(
        default_factory=list,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
