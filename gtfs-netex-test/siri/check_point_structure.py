from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDuration

from .accessibility_feature_enumeration_1 import AccessibilityFeatureEnumeration1
from .check_point_process_enumeration import CheckPointProcessEnumeration
from .check_point_service_enumeration import CheckPointServiceEnumeration
from .congestion_enumeration import CongestionEnumeration
from .validity_condition_structure import ValidityConditionStructure

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass(kw_only=True)
class CheckPointStructure:
    check_point_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CheckPointId",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        },
    )
    validity_condition: Optional[ValidityConditionStructure] = field(
        default=None,
        metadata={
            "name": "ValidityCondition",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        },
    )
    check_point_process: Optional[CheckPointProcessEnumeration] = field(
        default=None,
        metadata={
            "name": "CheckPointProcess",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        },
    )
    check_point_service: Optional[CheckPointServiceEnumeration] = field(
        default=None,
        metadata={
            "name": "CheckPointService",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        },
    )
    access_feature_type: Optional[AccessibilityFeatureEnumeration1] = field(
        default=None,
        metadata={
            "name": "AccessFeatureType",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        },
    )
    congestion: Optional[CongestionEnumeration] = field(
        default=None,
        metadata={
            "name": "Congestion",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        },
    )
    facility_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "FacilityRef",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        },
    )
    minimum_likely_delay: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MinimumLikelyDelay",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        },
    )
    average_delay: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "AverageDelay",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        },
    )
    maximum_likely_delay: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MaximumLikelyDelay",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        },
    )
