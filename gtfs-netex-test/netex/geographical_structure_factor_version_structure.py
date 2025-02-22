from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional, Union

from .distance_matrix_element_ref import DistanceMatrixElementRef
from .geographical_interval_ref import GeographicalIntervalRef
from .geographical_unit_ref import GeographicalUnitRef
from .parking_tariff_ref import ParkingTariffRef
from .priceable_object_version_structure import FareStructureFactorVersionStructure
from .tariff_ref import TariffRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class GeographicalStructureFactorVersionStructure(FareStructureFactorVersionStructure):
    class Meta:
        name = "GeographicalStructureFactor_VersionStructure"

    tariff_ref: Optional[Union[ParkingTariffRef, TariffRef]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ParkingTariffRef",
                    "type": ParkingTariffRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TariffRef",
                    "type": TariffRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    geographical_interval_ref: Optional[GeographicalIntervalRef] = field(
        default=None,
        metadata={
            "name": "GeographicalIntervalRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    distance_matrix_element_ref: Optional[DistanceMatrixElementRef] = field(
        default=None,
        metadata={
            "name": "DistanceMatrixElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    geographical_unit_ref: Optional[GeographicalUnitRef] = field(
        default=None,
        metadata={
            "name": "GeographicalUnitRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    number_of_units_or_amount_factor: Optional[Union[int, Decimal]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "NumberOfUnits",
                    "type": int,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AmountFactor",
                    "type": Decimal,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
