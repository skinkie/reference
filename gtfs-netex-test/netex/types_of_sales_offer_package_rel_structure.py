from dataclasses import dataclass, field
from typing import Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .type_of_sales_offer_package import TypeOfSalesOfferPackage
from .type_of_sales_offer_package_ref import TypeOfSalesOfferPackageRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TypesOfSalesOfferPackageRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "typesOfSalesOfferPackage_RelStructure"

    type_of_sales_offer_package_ref_or_type_of_sales_offer_package: list[Union[TypeOfSalesOfferPackageRef, TypeOfSalesOfferPackage]] = field(
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
        },
    )
