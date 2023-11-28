from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDuration
from netex.entitlement_constraint_structure import EntitlementConstraintStructure
from netex.sales_offer_package_ref import SalesOfferPackageRef
from netex.usage_parameter_version_structure import UsageParameterVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SalesOfferPackageEntitlementRequiredVersionStructure(UsageParameterVersionStructure):
    """
    Type for SALES OFFER PACKAGE ENTITLEMENT REQUIRED.

    :ivar sales_offer_package_ref:
    :ivar minimum_qualification_period: Minimum duration  that required
        product must be held to be eligible.
    :ivar entitlement_constraint: Limits on choices associated with
        entitlement +v1.1
    """
    class Meta:
        name = "SalesOfferPackageEntitlementRequired_VersionStructure"

    sales_offer_package_ref: Optional[SalesOfferPackageRef] = field(
        default=None,
        metadata={
            "name": "SalesOfferPackageRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
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
