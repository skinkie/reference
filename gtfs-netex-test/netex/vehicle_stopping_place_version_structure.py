from dataclasses import dataclass, field
from typing import Optional, Union

from .railway_link_ref import RailwayLinkRef
from .railway_point_ref import RailwayPointRef
from .road_link_ref import RoadLinkRef
from .road_point_ref import RoadPointRef
from .stop_place_space_version_structure import StopPlaceSpaceVersionStructure
from .vehicle_quay_alignments_rel_structure import VehicleQuayAlignmentsRelStructure
from .vehicle_stopping_positions_rel_structure import VehicleStoppingPositionsRelStructure
from .wire_link_ref import WireLinkRef
from .wire_point_ref import WirePointRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class VehicleStoppingPlaceVersionStructure(StopPlaceSpaceVersionStructure):
    class Meta:
        name = "VehicleStoppingPlace_VersionStructure"

    infrastructure_link_ref: Optional[Union[WireLinkRef, RoadLinkRef, RailwayLinkRef]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "WireLinkRef",
                    "type": WireLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoadLinkRef",
                    "type": RoadLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RailwayLinkRef",
                    "type": RailwayLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    infrastructure_point_ref: Optional[Union[WirePointRef, RoadPointRef, RailwayPointRef]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "WirePointRef",
                    "type": WirePointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoadPointRef",
                    "type": RoadPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RailwayPointRef",
                    "type": RailwayPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    vehicle_stopping_positions: Optional[VehicleStoppingPositionsRelStructure] = field(
        default=None,
        metadata={
            "name": "vehicleStoppingPositions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    quay_alignments: Optional[VehicleQuayAlignmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "quayAlignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
