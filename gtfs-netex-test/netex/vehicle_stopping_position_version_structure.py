from dataclasses import dataclass, field
from typing import Optional
from netex.multilingual_string import MultilingualString
from netex.relation_to_vehicle_enumeration import RelationToVehicleEnumeration
from netex.stop_place_component_version_structure import StopPlaceComponentVersionStructure
from netex.vehicle_position_alignments_rel_structure import VehiclePositionAlignmentsRelStructure
from netex.vehicle_stopping_place_ref import VehicleStoppingPlaceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleStoppingPositionVersionStructure(StopPlaceComponentVersionStructure):
    """
    Type for a VEHICLE STOPPING POSITION.

    :ivar vehicle_stopping_place_ref:
    :ivar label: Additional Label of a VEHICLE STOPPING POSITION.
    :ivar relation_to_vehicle: Relationship of position to VHEICLE.
    :ivar bearing: Bearing of vehicle in position in absolute degrees
        against North.
    :ivar vehicle_position_alignments: BOARDING POSITIONs with which
        VEHICLE STOPPING POSITION. aligns.
    """
    class Meta:
        name = "VehicleStoppingPosition_VersionStructure"

    vehicle_stopping_place_ref: Optional[VehicleStoppingPlaceRef] = field(
        default=None,
        metadata={
            "name": "VehicleStoppingPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    label: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Label",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    relation_to_vehicle: Optional[RelationToVehicleEnumeration] = field(
        default=None,
        metadata={
            "name": "RelationToVehicle",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    bearing: Optional[int] = field(
        default=None,
        metadata={
            "name": "Bearing",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_position_alignments: Optional[VehiclePositionAlignmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "vehiclePositionAlignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
