from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDuration

from .entitlement_constraint_structure import EntitlementConstraintStructure
from .entitlement_type_enumeration import EntitlementTypeEnumeration
from .sales_offer_package_ref import SalesOfferPackageRef
from .usage_parameter_version_structure import UsageParameterVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SalesOfferPackageEntitlementGivenVersionStructure(UsageParameterVersionStructure):
    class Meta:
        name = "SalesOfferPackageEntitlementGiven_VersionStructure"

    sales_offer_package_ref: Optional[SalesOfferPackageRef] = field(
        default=None,
        metadata={
            "name": "SalesOfferPackageRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    minimum_qualification_period: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MinimumQualificationPeriod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    entitlement_constraint: Optional[EntitlementConstraintStructure] = field(
        default=None,
        metadata={
            "name": "EntitlementConstraint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    entitlement_type: Optional[EntitlementTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "EntitlementType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
