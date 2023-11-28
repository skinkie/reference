from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlTime
from netex.block_part_version_structure import BlockPartVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TrainBlockPartVersionStructure(BlockPartVersionStructure):
    """
    Type for TRAIN BLOCK PART.

    :ivar start_time: Start time of BLOCK PART- In principle this can be
        derived from the Start time of the first journey and the
        preparation duration but may be stated  explicitly as well.
    :ivar start_time_day_offset: Day offset of Start time from current
        OPERATING DAY.
    :ivar end_time: End time of BLOCK PART. In principle this can be
        derived from the Start time of the last journey and the
        finishing duration but may be stated  explicitly as well.
    :ivar end_time_day_offset: Day offset of end time from current
        OPERATING DAY.
    :ivar type_of_coupling: Type of Coupling.
    """
    class Meta:
        name = "TrainBlockPart_VersionStructure"

    start_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "StartTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    start_time_day_offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "StartTimeDayOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    end_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "EndTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    end_time_day_offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "EndTimeDayOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_coupling: Optional[str] = field(
        default=None,
        metadata={
            "name": "TypeOfCoupling",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
