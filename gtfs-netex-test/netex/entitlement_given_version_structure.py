from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDuration
from netex.amount_of_price_unit_product_ref import AmountOfPriceUnitProductRef
from netex.capped_discount_right_ref import CappedDiscountRightRef
from netex.entitlement_constraint_structure import EntitlementConstraintStructure
from netex.entitlement_product_ref import EntitlementProductRef
from netex.entitlement_type_enumeration import EntitlementTypeEnumeration
from netex.fare_product_ref import FareProductRef
from netex.preassigned_fare_product_ref import PreassignedFareProductRef
from netex.sale_discount_right_ref import SaleDiscountRightRef
from netex.service_access_right_ref import ServiceAccessRightRef
from netex.supplement_product_ref import SupplementProductRef
from netex.third_party_product_ref import ThirdPartyProductRef
from netex.usage_discount_right_ref import UsageDiscountRightRef
from netex.usage_parameter_version_structure import UsageParameterVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class EntitlementGivenVersionStructure(UsageParameterVersionStructure):
    """
    Type for ENTITLEMENT GIVEN.

    :ivar choice:
    :ivar minimum_qualification_period: Minimum duration  that required
        product must be held to be eligible.
    :ivar entitlement_constraint: Limits on choices associated with
        entitlement +v1.1
    :ivar entitlement_type: Type of Entitlement given.
    """
    class Meta:
        name = "EntitlementGiven_VersionStructure"

    choice: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "EntitlementProductRef",
                    "type": EntitlementProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SupplementProductRef",
                    "type": SupplementProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PreassignedFareProductRef",
                    "type": PreassignedFareProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AmountOfPriceUnitProductRef",
                    "type": AmountOfPriceUnitProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UsageDiscountRightRef",
                    "type": UsageDiscountRightRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ThirdPartyProductRef",
                    "type": ThirdPartyProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CappedDiscountRightRef",
                    "type": CappedDiscountRightRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SaleDiscountRightRef",
                    "type": SaleDiscountRightRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareProductRef",
                    "type": FareProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceAccessRightRef",
                    "type": ServiceAccessRightRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    minimum_qualification_period: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MinimumQualificationPeriod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    entitlement_constraint: Optional[EntitlementConstraintStructure] = field(
        default=None,
        metadata={
            "name": "EntitlementConstraint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    entitlement_type: Optional[EntitlementTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "EntitlementType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
