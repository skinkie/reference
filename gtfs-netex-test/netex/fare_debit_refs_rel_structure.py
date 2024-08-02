from dataclasses import dataclass, field
from typing import List, Union

from .booking_debit_ref import BookingDebitRef
from .fare_debit_ref import FareDebitRef
from .fare_product_sale_debit_ref import FareProductSaleDebitRef
from .offence_debit_ref import OffenceDebitRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .other_debit_ref import OtherDebitRef
from .trip_debit_ref import TripDebitRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareDebitRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "fareDebitRefs_RelStructure"

    fare_debit_ref: List[Union[OffenceDebitRef, FareProductSaleDebitRef, TripDebitRef, BookingDebitRef, OtherDebitRef, FareDebitRef]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "OffenceDebitRef",
                    "type": OffenceDebitRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareProductSaleDebitRef",
                    "type": FareProductSaleDebitRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TripDebitRef",
                    "type": TripDebitRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BookingDebitRef",
                    "type": BookingDebitRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OtherDebitRef",
                    "type": OtherDebitRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareDebitRef",
                    "type": FareDebitRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
