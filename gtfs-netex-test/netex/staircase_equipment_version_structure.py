from dataclasses import dataclass, field
from typing import Optional
from netex.stair_equipment_version_structure import StairEquipmentVersionStructure
from netex.stair_flights_rel_structure import StairFlightsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class StaircaseEquipmentVersionStructure(StairEquipmentVersionStructure):
    """
    Type for a STAIRCASE EQUIPMENT.

    :ivar continuous_handrail: Whether Handrail is continuous across
        staircase.
    :ivar without_riser: Whether openwork stairs (no riser). +v1.1
    :ivar spiral_stair: Whether Stairs are spiral.
    :ivar number_of_flights: Number of flights of Stairs.
    :ivar flights: Flight of stairs.
    """
    class Meta:
        name = "StaircaseEquipment_VersionStructure"

    continuous_handrail: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ContinuousHandrail",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    without_riser: Optional[bool] = field(
        default=None,
        metadata={
            "name": "WithoutRiser",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    spiral_stair: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SpiralStair",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    number_of_flights: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfFlights",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    flights: Optional[StairFlightsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
