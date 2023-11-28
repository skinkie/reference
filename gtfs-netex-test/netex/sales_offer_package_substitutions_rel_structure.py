from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.sales_offer_package_substitution import SalesOfferPackageSubstitution
from netex.sales_offer_package_substitution_ref import SalesOfferPackageSubstitutionRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SalesOfferPackageSubstitutionsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of SALES OFFER PACKAGE SUBSTITUTIONs.
    """
    class Meta:
        name = "salesOfferPackageSubstitutions_RelStructure"

    sales_offer_package_substitution_ref_or_sales_offer_package_substitution: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "SalesOfferPackageSubstitutionRef",
                    "type": SalesOfferPackageSubstitutionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesOfferPackageSubstitution",
                    "type": SalesOfferPackageSubstitution,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
