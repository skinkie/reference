from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.fare_demand_factor_ref import FareDemandFactorRef
from netex.fare_quota_factor_ref import FareQuotaFactorRef
from netex.fare_structure_factor import FareStructureFactor
from netex.geographical_structure_factor_ref import GeographicalStructureFactorRef
from netex.parking_charge_band_ref import ParkingChargeBandRef
from netex.quality_structure_factor_ref import QualityStructureFactorRef
from netex.time_structure_factor_ref import TimeStructureFactorRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FareStructureFactorsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of FARE STRUCTURE FACTORs.
    """
    class Meta:
        name = "fareStructureFactors_RelStructure"

    choice: List[object] = field(
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
                    "name": "FareQuotaFactorRef",
                    "type": FareQuotaFactorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareDemandFactorRef",
                    "type": FareDemandFactorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "QualityStructureFactorRef",
                    "type": QualityStructureFactorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeographicalStructureFactorRef",
                    "type": GeographicalStructureFactorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareStructureFactor",
                    "type": FareStructureFactor,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
