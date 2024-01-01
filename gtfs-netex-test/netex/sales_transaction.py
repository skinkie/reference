from dataclasses import dataclass
from .sales_transaction_version_structure import (
    SalesTransactionVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SalesTransaction(SalesTransactionVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    validity_conditions: RestrictedVar
    valid_between: RestrictedVar
    alternative_texts: RestrictedVar
