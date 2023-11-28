from dataclasses import dataclass, field
from typing import List
from netex.parking_charge_band_ref import ParkingChargeBandRef
from netex.strict_containment_aggregation_structure import StrictContainmentAggregationStructure
from netex.time_structure_factor import TimeStructureFactor
from netex.time_structure_factor_ref import TimeStructureFactorRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TimeStructureFactorsRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of TIME STRUCTURE FACTOR.
    """
    class Meta:
        name = "timeStructureFactors_RelStructure"

    parking_charge_band_ref_or_time_structure_factor_ref_or_time_structure_factor: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ParkingChargeBandRef",
                    "type": ParkingChargeBandRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeStructureFactorRef",
                    "type": TimeStructureFactorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeStructureFactor",
                    "type": TimeStructureFactor,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
