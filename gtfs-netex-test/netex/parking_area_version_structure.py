from dataclasses import dataclass, field
from typing import Optional
from netex.entrance_refs_rel_structure import EntranceRefsRelStructure
from netex.parking_bays_rel_structure import ParkingBaysRelStructure
from netex.parking_component_version_structure import ParkingComponentVersionStructure
from netex.parking_properties import ParkingProperties
from netex.parking_properties_rel_structure import ParkingPropertiesRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ParkingAreaVersionStructure(ParkingComponentVersionStructure):
    """
    Type for a PARKING AREA.

    :ivar total_capacity: Total number of parking places in PARKING
        AREA.
    :ivar number_of_bays_with_recharging: Total number of parking places
        supportig Electirc car recharging  in PARKING AREA.
    :ivar parking_properties_or_parking_properties:
    :ivar bays: Bays within PARKING AREA.
    :ivar entrances: ENTRANCEs to PARKING AREA.
    """
    class Meta:
        name = "ParkingArea_VersionStructure"

    total_capacity: Optional[int] = field(
        default=None,
        metadata={
            "name": "TotalCapacity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    number_of_bays_with_recharging: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfBaysWithRecharging",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parking_properties_or_parking_properties: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ParkingProperties",
                    "type": ParkingProperties,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "parkingProperties",
                    "type": ParkingPropertiesRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    bays: Optional[ParkingBaysRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    entrances: Optional[EntranceRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
