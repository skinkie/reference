from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from .quality_index_enumeration import QualityIndexEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class PredictionQualityStructure:
    prediction_level: QualityIndexEnumeration = field(
        metadata={
            "name": "PredictionLevel",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    percentile: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Percentile",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    lower_time_limit: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "LowerTimeLimit",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    higher_time_limit: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "HigherTimeLimit",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
