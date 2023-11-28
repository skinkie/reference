from dataclasses import dataclass, field
from netex.timetable_version_frame_structure import TimetableVersionFrameStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TimetableFrame(TimetableVersionFrameStructure):
    """
    A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the
    same VALIDITY CONDITIONs have been assigned.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
