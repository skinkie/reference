from dataclasses import dataclass, field
from typing import ForwardRef, List, Optional, Union

from xsdata.models.datatype import XmlDateTime, XmlDuration

from .destination_ref_structure import DestinationRefStructure
from .direction_ref_structure import DirectionRefStructure
from .extensions_1 import Extensions1
from .include_translations import IncludeTranslations
from .line_ref_structure import LineRefStructure
from .monitoring_ref_structure import MonitoringRefStructure
from .operator_ref_structure import OperatorRefStructure
from .stop_monitoring_detail_enumeration import StopMonitoringDetailEnumeration
from .stop_visit_type_enumeration import StopVisitTypeEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class StopMonitoringFilterStructure:
    preview_interval: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "PreviewInterval",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    start_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "StartTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    monitoring_ref: MonitoringRefStructure = field(
        metadata={
            "name": "MonitoringRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    operator_ref: Optional[OperatorRefStructure] = field(
        default=None,
        metadata={
            "name": "OperatorRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    line_ref: Optional[LineRefStructure] = field(
        default=None,
        metadata={
            "name": "LineRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    direction_ref: Optional[DirectionRefStructure] = field(
        default=None,
        metadata={
            "name": "DirectionRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    destination_ref: Optional[DestinationRefStructure] = field(
        default=None,
        metadata={
            "name": "DestinationRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_visit_types: Optional[StopVisitTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "StopVisitTypes",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    language: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Language",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    include_translations: Optional[IncludeTranslations] = field(
        default=None,
        metadata={
            "name": "IncludeTranslations",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    maximum_stop_visits: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaximumStopVisits",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    minimum_stop_visits_per_line_or_minimum_stop_visits_per_line_via: Optional[Union["StopMonitoringFilterStructure.MinimumStopVisitsPerLine", "StopMonitoringFilterStructure.MinimumStopVisitsPerLineVia"]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "MinimumStopVisitsPerLine",
                    "type": ForwardRef("StopMonitoringFilterStructure.MinimumStopVisitsPerLine"),
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "MinimumStopVisitsPerLineVia",
                    "type": ForwardRef("StopMonitoringFilterStructure.MinimumStopVisitsPerLineVia"),
                    "namespace": "http://www.siri.org.uk/siri",
                },
            ),
        },
    )
    maximum_text_length: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaximumTextLength",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_monitoring_detail_level: Optional[StopMonitoringDetailEnumeration] = field(
        default=None,
        metadata={
            "name": "StopMonitoringDetailLevel",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    include_situations: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IncludeSituations",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    maximum_number_of_calls: Optional["StopMonitoringFilterStructure.MaximumNumberOfCalls"] = field(
        default=None,
        metadata={
            "name": "MaximumNumberOfCalls",
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

    @dataclass(kw_only=True)
    class MaximumNumberOfCalls:
        previous: Optional[int] = field(
            default=None,
            metadata={
                "name": "Previous",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        onwards: Optional[int] = field(
            default=None,
            metadata={
                "name": "Onwards",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )

    @dataclass(kw_only=True)
    class MinimumStopVisitsPerLine:
        value: int = field(
            metadata={
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class MinimumStopVisitsPerLineVia:
        value: int = field(
            metadata={
                "required": True,
            }
        )
