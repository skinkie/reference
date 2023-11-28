from dataclasses import dataclass, field
from typing import Optional
from netex.access_equipment_version_structure import AccessEquipmentVersionStructure
from netex.crossing_type_enumeration import CrossingTypeEnumeration
from netex.tactile_warning_strip_enumeration import TactileWarningStripEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CrossingEquipmentVersionStructure(AccessEquipmentVersionStructure):
    """
    Type for a CROSSING EQUIPMENT.

    :ivar crossing_type: Type of CROSSING.
    :ivar zebra_crossing: Whether CROSSING is marked as Zebra.
    :ivar pedestrian_lights: Whether there are lights for pedestrians to
        cross by.
    :ivar acoustic_device_sensors: Whether crossing has Acoustic Device
        sensors.
    :ivar acoustic_crossing_aids: Whether crossing has Acoustic Crossing
        aids.
    :ivar tactile_guidance_strips: Whether crossing has tactile guidance
        strips.
    :ivar tactile_warning_strip: Whether crossing has tactile warning
        strip. +v1.1
    :ivar visual_guidance_bands: Whether crossing has visual guidance
        bands or guidance strips.
    :ivar dropped_kerb: Whether crossing has dropped Kerb.
    :ivar suitable_for_cycles: Whether equipment is suitable for cycles.
    """
    class Meta:
        name = "CrossingEquipment_VersionStructure"

    crossing_type: Optional[CrossingTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "CrossingType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    zebra_crossing: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ZebraCrossing",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    pedestrian_lights: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PedestrianLights",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    acoustic_device_sensors: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AcousticDeviceSensors",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    acoustic_crossing_aids: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AcousticCrossingAids",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    tactile_guidance_strips: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TactileGuidanceStrips",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    tactile_warning_strip: Optional[TactileWarningStripEnumeration] = field(
        default=None,
        metadata={
            "name": "TactileWarningStrip",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    visual_guidance_bands: Optional[bool] = field(
        default=None,
        metadata={
            "name": "VisualGuidanceBands",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    dropped_kerb: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DroppedKerb",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    suitable_for_cycles: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SuitableForCycles",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
