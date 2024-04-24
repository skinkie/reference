from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlTime

from .check_constraint_ref import CheckConstraintRef
from .check_process_type_enumeration import CheckProcessTypeEnumeration
from .multilingual_string import MultilingualString
from .passing_time_versioned_child_structure import PassingTimeVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PassengerAtStopTimeVersionedChildStructure(PassingTimeVersionedChildStructure):
    class Meta:
        name = "PassengerAtStopTime_VersionedChildStructure"

    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    earliest_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "EarliestTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    earliest_day_offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "EarliestDayOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    latest_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "LatestTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    latest_day_offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "LatestDayOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    check_constraint_ref: Optional[CheckConstraintRef] = field(
        default=None,
        metadata={
            "name": "CheckConstraintRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    check_constraint_process: Optional[CheckProcessTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "CheckConstraintProcess",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
