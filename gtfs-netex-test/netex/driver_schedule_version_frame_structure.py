from dataclasses import dataclass, field
from typing import Optional
from netex.common_version_frame_structure import CommonVersionFrameStructure
from netex.driver_trips_in_frame_rel_structure import DriverTripsInFrameRelStructure
from netex.duties_in_frame_rel_structure import DutiesInFrameRelStructure
from netex.duty_parts_in_frame_rel_structure import DutyPartsInFrameRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DriverScheduleVersionFrameStructure(CommonVersionFrameStructure):
    """
    Type for a DRIVER SCHEDULE FRAME.

    :ivar duties: DUTIes in frame.
    :ivar duty_parts: DUTY PARTs (Runs) in frame.
    :ivar driver_trips: DRIVER TRIPs in frame.
    """
    class Meta:
        name = "DriverSchedule_VersionFrameStructure"

    duties: Optional[DutiesInFrameRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    duty_parts: Optional[DutyPartsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "dutyParts",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    driver_trips: Optional[DriverTripsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "driverTrips",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
