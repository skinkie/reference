from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDuration
from netex.point_version_structure import PointVersionStructure
from netex.timing_point_status_enumeration import TimingPointStatusEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TimingPointVersionStructure(PointVersionStructure):
    """
    Type for TIMING POINT.

    :ivar timing_point_status: Default Nature of TIMING POINT. Default
        is primary TIMING POINT.
    :ivar allowed_for_wait_time: Default WAIT TIME associated with
        TIMING POINT. May be overridden on specific POINTs in JOURNEY
        PATTERNs for POINT.
    """
    class Meta:
        name = "TimingPoint_VersionStructure"

    timing_point_status: Optional[TimingPointStatusEnumeration] = field(
        default=None,
        metadata={
            "name": "TimingPointStatus",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    allowed_for_wait_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "AllowedForWaitTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
