from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDate
from netex.assignment_version_structure_1 import AssignmentVersionStructure1
from netex.day_type_ref import DayTypeRef
from netex.fare_day_type_ref import FareDayTypeRef
from netex.operating_day_ref import OperatingDayRef
from netex.operating_period_ref import OperatingPeriodRef
from netex.service_calendar_ref import ServiceCalendarRef
from netex.timeband_ref import TimebandRef
from netex.uic_operating_period_ref import UicOperatingPeriodRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DayTypeAssignmentVersionStructure(AssignmentVersionStructure1):
    """
    Type for a DAY TYPE ASSIGNMENT.

    :ivar service_calendar_ref: Reference to parent Calendar. If given
        by context does not need to be given.
    :ivar choice:
    :ivar fare_day_type_ref_or_day_type_ref:
    :ivar timeband_ref:
    :ivar is_available: Whether availabel on assigned day
    """
    class Meta:
        name = "DayTypeAssignment_VersionStructure"

    service_calendar_ref: Optional[ServiceCalendarRef] = field(
        default=None,
        metadata={
            "name": "ServiceCalendarRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    choice: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "UicOperatingPeriodRef",
                    "type": UicOperatingPeriodRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OperatingPeriodRef",
                    "type": OperatingPeriodRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OperatingDayRef",
                    "type": OperatingDayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Date",
                    "type": XmlDate,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    fare_day_type_ref_or_day_type_ref: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FareDayTypeRef",
                    "type": FareDayTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DayTypeRef",
                    "type": DayTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    timeband_ref: List[TimebandRef] = field(
        default_factory=list,
        metadata={
            "name": "TimebandRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 5,
        }
    )
    is_available: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isAvailable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
