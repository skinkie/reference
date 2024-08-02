from dataclasses import dataclass, field
from typing import List, Optional

from xsdata.models.datatype import XmlDateTime

from .extension_type import ExtensionType
from .header_information import HeaderInformation
from .overall_severity_enum import OverallSeverityEnum
from .situation_record import SituationRecord

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class Situation:
    overall_severity: Optional[OverallSeverityEnum] = field(
        default=None,
        metadata={
            "name": "overallSeverity",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    related_situation: List[str] = field(
        default_factory=list,
        metadata={
            "name": "relatedSituation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_length": 1024,
        },
    )
    situation_version: Optional[int] = field(
        default=None,
        metadata={
            "name": "situationVersion",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    situation_version_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "situationVersionTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    header_information: HeaderInformation = field(
        metadata={
            "name": "headerInformation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    situation_record: List[SituationRecord] = field(
        default_factory=list,
        metadata={
            "name": "situationRecord",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "min_occurs": 1,
        },
    )
    situation_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "situationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
