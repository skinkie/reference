from dataclasses import dataclass, field
from typing import Optional

from .amount_of_price_unit_refs_rel_structure import AmountOfPriceUnitRefsRelStructure
from .discount_right_refs_rel_structure import DiscountRightRefsRelStructure
from .fare_element_in_sequence_refs_rel_structure import FareElementInSequenceRefsRelStructure
from .fare_structure_element_refs_rel_structure import FareStructureElementRefsRelStructure
from .priceable_object_version_structure import PriceableObjectVersionStructure
from .third_party_product_refs_rel_structure import ThirdPartyProductRefsRelStructure
from .validable_element_prices_rel_structure import ValidableElementPricesRelStructure
from .validity_parameter_assignments_rel_structure import ValidityParameterAssignmentsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ValidableElementVersionStructure(PriceableObjectVersionStructure):
    class Meta:
        name = "ValidableElement_VersionStructure"

    fare_structure_elements: Optional[FareStructureElementRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "fareStructureElements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    fare_elements_in_sequence: Optional[FareElementInSequenceRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "fareElementsInSequence",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    discount_rights: Optional[DiscountRightRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "discountRights",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    amount_of_price_units: Optional[AmountOfPriceUnitRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "amountOfPriceUnits",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    third_party_products: Optional[ThirdPartyProductRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "thirdPartyProducts",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    validity_parameter_assignments: Optional[ValidityParameterAssignmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "validityParameterAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    prices: Optional[ValidableElementPricesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
