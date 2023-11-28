from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from netex.baggage_type_enumeration import BaggageTypeEnumeration
from netex.baggage_use_type_enumeration import BaggageUseTypeEnumeration
from netex.luggage_allowance_type_enumeration import LuggageAllowanceTypeEnumeration
from netex.luggage_charging_basis_enumeration import LuggageChargingBasisEnumeration
from netex.usage_parameter_version_structure import UsageParameterVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class LuggageAllowanceVersionStructure(UsageParameterVersionStructure):
    """
    Type for LUGGAGE ALLOWANCE.

    :ivar baggage_use_type: Type of Baggage use.
    :ivar baggage_type: Type of Baggage described by this allowance.
    :ivar luggage_allowance_type: Summary of luggage allowance type.
    :ivar maximum_number_items: Maximum number of items allowed for
        hand luggage.
    :ivar maximum_bag_height: Maximum height of a bag.
    :ivar maximum_bag_width: Maximum width of a bag.
    :ivar maximum_bag_depth: Maximum depth of a bag.
    :ivar maximum_bag_weight: Maximum weight of a bag.
    :ivar total_weight: Maximum weight of a bag.
    :ivar luggage_charging_basis: Basis on which lugggage is charged.
    """
    class Meta:
        name = "LuggageAllowance_VersionStructure"

    baggage_use_type: Optional[BaggageUseTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "BaggageUseType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    baggage_type: Optional[BaggageTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "BaggageType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    luggage_allowance_type: Optional[LuggageAllowanceTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "LuggageAllowanceType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximum_number_items: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaximumNumberItems",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximum_bag_height: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaximumBagHeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximum_bag_width: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaximumBagWidth",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximum_bag_depth: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaximumBagDepth",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximum_bag_weight: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaximumBagWeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    total_weight: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TotalWeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    luggage_charging_basis: Optional[LuggageChargingBasisEnumeration] = field(
        default=None,
        metadata={
            "name": "LuggageChargingBasis",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
