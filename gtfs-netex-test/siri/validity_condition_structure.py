from dataclasses import dataclass, field
from typing import List, Optional

from xsdata.models.datatype import XmlDateTime

from .timeband_structure import TimebandStructure

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass(kw_only=True)
class ValidityConditionStructure:
    from_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "FromDateTime",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        },
    )
    to_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ToDateTime",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        },
    )
    day_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "DayType",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        },
    )
    timebands: List["ValidityConditionStructure.Timebands"] = field(
        default_factory=list,
        metadata={
            "name": "Timebands",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        },
    )

    @dataclass(kw_only=True)
    class Timebands:
        timeband: TimebandStructure = field(
            metadata={
                "name": "Timeband",
                "type": "Element",
                "namespace": "http://www.ifopt.org.uk/ifopt",
                "required": True,
            }
        )
