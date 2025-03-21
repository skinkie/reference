from dataclasses import dataclass, field
from typing import Union

from .parking_charge_band_ref import ParkingChargeBandRef
from .strict_containment_aggregation_structure import StrictContainmentAggregationStructure
from .time_structure_factor import TimeStructureFactor
from .time_structure_factor_ref import TimeStructureFactorRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TimeStructureFactorsRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "timeStructureFactors_RelStructure"

    parking_charge_band_ref_or_time_structure_factor_ref_or_time_structure_factor: list[Union[ParkingChargeBandRef, TimeStructureFactorRef, TimeStructureFactor]] = field(
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
        },
    )
