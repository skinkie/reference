from dataclasses import dataclass, field
from typing import Optional, Union

from .access_right_parameter_assignment_version_structure import AccessRightParameterAssignmentVersionStructure
from .fare_demand_factor_ref import FareDemandFactorRef
from .fare_quota_factor_ref import FareQuotaFactorRef
from .geographical_interval_ref import GeographicalIntervalRef
from .geographical_structure_factor_ref import GeographicalStructureFactorRef
from .parking_charge_band_ref import ParkingChargeBandRef
from .quality_structure_factor_ref import QualityStructureFactorRef
from .time_interval_ref import TimeIntervalRef
from .time_structure_factor_ref import TimeStructureFactorRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ValidityParameterAssignmentVersionStructure(AccessRightParameterAssignmentVersionStructure):
    class Meta:
        name = "ValidityParameterAssignment_VersionStructure"

    time_interval_ref_or_parking_charge_band_ref_or_time_structure_factor_ref: Optional[Union[TimeIntervalRef, ParkingChargeBandRef, TimeStructureFactorRef]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TimeIntervalRef",
                    "type": TimeIntervalRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
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
            ),
        },
    )
    geographical_interval_ref_or_geographical_structure_factor_ref: Optional[Union[GeographicalIntervalRef, GeographicalStructureFactorRef]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "GeographicalIntervalRef",
                    "type": GeographicalIntervalRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeographicalStructureFactorRef",
                    "type": GeographicalStructureFactorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    quality_structure_factor_ref: Optional[Union[FareQuotaFactorRef, FareDemandFactorRef, QualityStructureFactorRef]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
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
            ),
        },
    )
