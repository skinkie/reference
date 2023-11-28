from dataclasses import dataclass, field
from typing import Optional
from netex.cell_versioned_child_structure import PriceableObjectVersionStructure
from netex.fulfilment_method_prices_rel_structure import FulfilmentMethodPricesRelStructure
from netex.fulfilment_method_type_enumeration import FulfilmentMethodTypeEnumeration
from netex.type_of_travel_document_refs_rel_structure import TypeOfTravelDocumentRefsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FulfilmentMethodVersionStructure(PriceableObjectVersionStructure):
    """
    Type for FULFILMENT METHOD.

    :ivar fulfilment_method_type: Classification of fulfilment method.
    :ivar requires_card: Whether use of of the method requires a credit
        or debit card.
    :ivar requires_booking_reference: Whether use of of the method
        requires  a booking reference.
    :ivar types_of_travel_document: TYPES OF TRAVEL DOCUMENT associated
        with method.
    :ivar prices: Prices for FULFILMENT METHOD.
    """
    class Meta:
        name = "FulfilmentMethod_VersionStructure"

    fulfilment_method_type: Optional[FulfilmentMethodTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "FulfilmentMethodType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    requires_card: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RequiresCard",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    requires_booking_reference: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RequiresBookingReference",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    types_of_travel_document: Optional[TypeOfTravelDocumentRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "typesOfTravelDocument",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    prices: Optional[FulfilmentMethodPricesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
