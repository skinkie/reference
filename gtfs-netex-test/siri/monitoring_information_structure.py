from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDuration

from .extensions_1 import Extensions1
from .monitoring_type_enumeration import MonitoringTypeEnumeration
from .monitoring_validity_condition_structure import MonitoringValidityConditionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class MonitoringInformationStructure:
    monitoring_interval: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MonitoringInterval",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    monitoring_type: Optional[MonitoringTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "MonitoringType",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    monitoring_period: Optional[MonitoringValidityConditionStructure] = field(
        default=None,
        metadata={
            "name": "MonitoringPeriod",
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
