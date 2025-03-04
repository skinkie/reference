from dataclasses import dataclass, field
from typing import Optional, Union

from .day_type_ref import DayTypeRef
from .entity_in_version_structure import DataManagedObjectStructure
from .fare_day_type_ref import FareDayTypeRef
from .month_validity_offsets_rel_structure import MonthValidityOffsetsRelStructure
from .multilingual_string import MultilingualString
from .price_unit_ref import PriceUnitRef
from .price_units_rel_structure import PriceUnitsRelStructure
from .pricing_rules_rel_structure import PricingRulesRelStructure
from .pricing_services_rel_structure import PricingServicesRelStructure
from .rounding_ref import RoundingRef
from .roundings_rel_structure import RoundingsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class PricingParameterSetVersionedStructure(DataManagedObjectStructure):
    class Meta:
        name = "PricingParameterSet_VersionedStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    price_unit_ref: Optional[PriceUnitRef] = field(
        default=None,
        metadata={
            "name": "PriceUnitRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    price_units: Optional[PriceUnitsRelStructure] = field(
        default=None,
        metadata={
            "name": "priceUnits",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    pricing_rules: Optional[PricingRulesRelStructure] = field(
        default=None,
        metadata={
            "name": "pricingRules",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    allow_cumulative_discounts: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AllowCumulativeDiscounts",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    rounding_ref: Optional[RoundingRef] = field(
        default=None,
        metadata={
            "name": "RoundingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    roundings: Optional[RoundingsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    day_type_ref: Optional[Union[FareDayTypeRef, DayTypeRef]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FareDayTypeRef",
                    "type": FareDayTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DayTypeRef",
                    "type": DayTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    month_validity_offsets: Optional[MonthValidityOffsetsRelStructure] = field(
        default=None,
        metadata={
            "name": "monthValidityOffsets",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    pricing_services: Optional[PricingServicesRelStructure] = field(
        default=None,
        metadata={
            "name": "pricingServices",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
