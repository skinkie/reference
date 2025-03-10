from dataclasses import dataclass, field
from typing import Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .meeting_restriction import MeetingRestriction
from .overtaking_possibility import OvertakingPossibility
from .restricted_manoeuvre import RestrictedManoeuvre
from .vehicle_type_at_point import VehicleTypeAtPoint

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class NetworkRestrictionsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "networkRestrictionsInFrame_RelStructure"

    network_restriction: list[Union[OvertakingPossibility, MeetingRestriction, RestrictedManoeuvre, VehicleTypeAtPoint]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "OvertakingPossibility",
                    "type": OvertakingPossibility,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MeetingRestriction",
                    "type": MeetingRestriction,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RestrictedManoeuvre",
                    "type": RestrictedManoeuvre,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleTypeAtPoint",
                    "type": VehicleTypeAtPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
