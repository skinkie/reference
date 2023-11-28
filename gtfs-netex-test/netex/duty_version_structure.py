from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDuration
from netex.alternative_texts_rel_structure import DataManagedObjectStructure
from netex.duty_parts_rel_structure import DutyPartsRelStructure
from netex.multilingual_string import MultilingualString
from netex.timetable_frame_ref import TimetableFrameRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DutyVersionStructure(DataManagedObjectStructure):
    """
    Type for DUTY.

    :ivar description: Description of DUTY.
    :ivar finishing_duration: Time to complete DUTY.
    :ivar preparation_duration: Time to complete DUTY.
    :ivar timetable_frame_ref:
    :ivar duty_parts: Parts of a DUTY.
    """
    class Meta:
        name = "Duty_VersionStructure"

    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    finishing_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "FinishingDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    preparation_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "PreparationDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    timetable_frame_ref: Optional[TimetableFrameRef] = field(
        default=None,
        metadata={
            "name": "TimetableFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    duty_parts: Optional[DutyPartsRelStructure] = field(
        default=None,
        metadata={
            "name": "dutyParts",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
