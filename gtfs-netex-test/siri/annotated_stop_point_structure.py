from dataclasses import dataclass, field
from typing import List, Optional, Union

from .line_direction_structure import LineDirectionStructure
from .line_ref_structure import LineRefStructure
from .location_structure import LocationStructure
from .natural_language_string_structure import NaturalLanguageStringStructure
from .service_feature_ref import ServiceFeatureRef
from .service_feature_structure import ServiceFeatureStructure
from .stop_area_ref_structure import StopAreaRefStructure
from .stop_point_ref_structure import StopPointRefStructure
from .timing_point import TimingPoint

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class AnnotatedStopPointStructure:
    stop_point_ref: StopPointRefStructure = field(
        metadata={
            "name": "StopPointRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    timing_point: Optional[TimingPoint] = field(
        default=None,
        metadata={
            "name": "TimingPoint",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    monitored: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Monitored",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "StopName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_area_ref: Optional[StopAreaRefStructure] = field(
        default=None,
        metadata={
            "name": "StopAreaRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    features: Optional["AnnotatedStopPointStructure.Features"] = field(
        default=None,
        metadata={
            "name": "Features",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    lines: Optional["AnnotatedStopPointStructure.Lines"] = field(
        default=None,
        metadata={
            "name": "Lines",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    location: Optional[LocationStructure] = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "name": "Url",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )

    @dataclass(kw_only=True)
    class Features:
        service_feature_or_service_feature_ref: List[Union[ServiceFeatureStructure, ServiceFeatureRef]] = field(
            default_factory=list,
            metadata={
                "type": "Elements",
                "choices": (
                    {
                        "name": "ServiceFeature",
                        "type": ServiceFeatureStructure,
                        "namespace": "http://www.siri.org.uk/siri",
                    },
                    {
                        "name": "ServiceFeatureRef",
                        "type": ServiceFeatureRef,
                        "namespace": "http://www.siri.org.uk/siri",
                    },
                ),
            },
        )

    @dataclass(kw_only=True)
    class Lines:
        line_ref_or_line_direction: List[Union[LineRefStructure, LineDirectionStructure]] = field(
            default_factory=list,
            metadata={
                "type": "Elements",
                "choices": (
                    {
                        "name": "LineRef",
                        "type": LineRefStructure,
                        "namespace": "http://www.siri.org.uk/siri",
                    },
                    {
                        "name": "LineDirection",
                        "type": LineDirectionStructure,
                        "namespace": "http://www.siri.org.uk/siri",
                    },
                ),
            },
        )
