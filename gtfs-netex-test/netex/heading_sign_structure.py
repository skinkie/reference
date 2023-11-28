from dataclasses import dataclass, field
from typing import Optional
from netex.all_vehicle_modes_of_transport_enumeration import AllVehicleModesOfTransportEnumeration
from netex.destination_display_ref import DestinationDisplayRef
from netex.direction_ref import DirectionRef
from netex.flexible_line_ref import FlexibleLineRef
from netex.line_ref import LineRef
from netex.multilingual_string import MultilingualString
from netex.sign_equipment_version_structure import SignEquipmentVersionStructure
from netex.transport_submode import TransportSubmode

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class HeadingSignStructure(SignEquipmentVersionStructure):
    """
    Type for a HEADING SIGN.

    :ivar place_name: Name of Stop.
    :ivar flexible_line_ref_or_line_ref:
    :ivar line_name: Content of Stop.
    :ivar transport_mode: Description of MODE of LINE.
    :ivar transport_submode:
    :ivar line_map: Graphic or sign for schematic map of lien from STOP
        PLACE.
    :ivar direction_ref:
    :ivar direction_name: Content of Stop.
    :ivar destination_display_ref:
    :ivar line_public_code: Public Code for Line.
    """
    place_name: MultilingualString = field(
        metadata={
            "name": "PlaceName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    flexible_line_ref_or_line_ref: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FlexibleLineRef",
                    "type": FlexibleLineRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LineRef",
                    "type": LineRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    line_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "LineName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    transport_mode: Optional[AllVehicleModesOfTransportEnumeration] = field(
        default=None,
        metadata={
            "name": "TransportMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    transport_submode: Optional[TransportSubmode] = field(
        default=None,
        metadata={
            "name": "TransportSubmode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    line_map: Optional[str] = field(
        default=None,
        metadata={
            "name": "LineMap",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    direction_ref: Optional[DirectionRef] = field(
        default=None,
        metadata={
            "name": "DirectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    direction_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "DirectionName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    destination_display_ref: Optional[DestinationDisplayRef] = field(
        default=None,
        metadata={
            "name": "DestinationDisplayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    line_public_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "LinePublicCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
