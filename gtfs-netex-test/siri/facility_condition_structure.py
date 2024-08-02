from dataclasses import dataclass, field
from typing import List, Optional, Union

from .extensions_1 import Extensions1
from .facility_ref import FacilityRef
from .facility_status_structure import FacilityStatusStructure
from .facility_structure import FacilityStructure
from .half_open_timestamp_output_range_structure import HalfOpenTimestampOutputRangeStructure
from .location_structure import LocationStructure
from .monitored_counting_structure import MonitoredCountingStructure
from .monitoring_information_structure import MonitoringInformationStructure
from .remedy_structure import RemedyStructure
from .situation_ref import SituationRef

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class FacilityConditionStructure:
    facility_or_facility_ref: Optional[Union[FacilityStructure, FacilityRef]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "Facility",
                    "type": FacilityStructure,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "FacilityRef",
                    "type": FacilityRef,
                    "namespace": "http://www.siri.org.uk/siri",
                },
            ),
        },
    )
    facility_status: FacilityStatusStructure = field(
        metadata={
            "name": "FacilityStatus",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    monitored_counting: List[MonitoredCountingStructure] = field(
        default_factory=list,
        metadata={
            "name": "MonitoredCounting",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    facility_updated_position: Optional[LocationStructure] = field(
        default=None,
        metadata={
            "name": "FacilityUpdatedPosition",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    situation_ref: Optional[SituationRef] = field(
        default=None,
        metadata={
            "name": "SituationRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    remedy: Optional[RemedyStructure] = field(
        default=None,
        metadata={
            "name": "Remedy",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    monitoring_info: Optional[MonitoringInformationStructure] = field(
        default=None,
        metadata={
            "name": "MonitoringInfo",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    validity_period: Optional[HalfOpenTimestampOutputRangeStructure] = field(
        default=None,
        metadata={
            "name": "ValidityPeriod",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    extensions: Optional[Extensions1] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
