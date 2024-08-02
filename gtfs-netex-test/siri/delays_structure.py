from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDuration

from .delay_band_enumeration import DelayBandEnumeration
from .delays_type_enum import DelaysTypeEnum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class DelaysStructure:
    delay_band: Optional[DelayBandEnumeration] = field(
        default=None,
        metadata={
            "name": "DelayBand",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    delay_type: Optional[DelaysTypeEnum] = field(
        default=None,
        metadata={
            "name": "DelayType",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    delay: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "Delay",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
