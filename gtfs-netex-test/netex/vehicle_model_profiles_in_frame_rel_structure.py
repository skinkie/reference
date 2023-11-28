from dataclasses import dataclass, field
from typing import List
from netex.car_model_profile import CarModelProfile
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.cycle_model_profile import CycleModelProfile

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleModelProfilesInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of VEHICLE MODEL  PROFILEs.
    """
    class Meta:
        name = "vehicleModelProfilesInFrame_RelStructure"

    car_model_profile_or_cycle_model_profile: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "CarModelProfile",
                    "type": CarModelProfile,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CycleModelProfile",
                    "type": CycleModelProfile,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
