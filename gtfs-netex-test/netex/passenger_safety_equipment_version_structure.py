from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from netex.audio_announcement_type_enumeration import AudioAnnouncementTypeEnumeration
from netex.audio_trigger_method_enumeration import AudioTriggerMethodEnumeration
from netex.lighting_enumeration import LightingEnumeration
from netex.passenger_equipment_version_structure import PassengerEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PassengerSafetyEquipmentVersionStructure(PassengerEquipmentVersionStructure):
    """
    Type for a PASSENGER SAFETY EQUIPMENT.

    :ivar cctv: Whether there is CCTV.
    :ivar mobile_phone_coverage: Whether lift there is mobile phone
        coverage.
    :ivar panic_button: Whether there is a panic button.
    :ivar sos_panel: Whether there is an SOS panel.
    :ivar height_of_sos_panel: Height of SOS panel.
    :ivar lighting: Type of Lighting in area.
    :ivar audio_announcements: Whether there are Audio Announcements.
        +v1.1
    :ivar acoustic_announcements: DEPRECATED - Renamed to
        AudioAnnouncements for consistency.  Old value kept for
        backwards compatibility - will be dropped in future release.
    :ivar audio_announcement_type: Triggering type for Audio
        Announcements. +v1.1
    :ivar audio_announcements_trigger: How to trigger Acoustic
        Announcements. +v1.1
    """
    class Meta:
        name = "PassengerSafetyEquipment_VersionStructure"

    cctv: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Cctv",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    mobile_phone_coverage: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MobilePhoneCoverage",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    panic_button: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PanicButton",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    sos_panel: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SosPanel",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    height_of_sos_panel: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "HeightOfSosPanel",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    lighting: Optional[LightingEnumeration] = field(
        default=None,
        metadata={
            "name": "Lighting",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    audio_announcements: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AudioAnnouncements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    acoustic_announcements: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AcousticAnnouncements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    audio_announcement_type: Optional[AudioAnnouncementTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "AudioAnnouncementType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    audio_announcements_trigger: Optional[AudioTriggerMethodEnumeration] = field(
        default=None,
        metadata={
            "name": "AudioAnnouncementsTrigger",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
