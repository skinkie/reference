from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.type_of_sales_offer_package import TypeOfSalesOfferPackage
from netex.type_of_sales_offer_package_ref import TypeOfSalesOfferPackageRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypesOfSalesOfferPackageRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of TYPE OF SALES OFFER PACKAGEs.
    """
    class Meta:
        name = "typesOfSalesOfferPackage_RelStructure"

    type_of_sales_offer_package_ref_or_type_of_sales_offer_package: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TypeOfSalesOfferPackageRef",
                    "type": TypeOfSalesOfferPackageRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfSalesOfferPackage",
                    "type": TypeOfSalesOfferPackage,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
