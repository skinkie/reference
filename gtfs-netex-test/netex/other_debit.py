from dataclasses import dataclass, field
from typing import Any

from .other_debit_version_structure import OtherDebitVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OtherDebit(OtherDebitVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    amount: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    currency: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    price_unit_ref: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    units: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    rule_step_results: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    payment_method: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    type_of_payment_method_ref: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    card_number: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    validity_conditions_or_valid_between: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    alternative_texts: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
