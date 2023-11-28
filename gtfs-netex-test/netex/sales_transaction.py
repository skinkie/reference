from dataclasses import dataclass, field
from netex.sales_transaction_version_structure import SalesTransactionVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SalesTransaction(SalesTransactionVersionStructure):
    """
    A SALE OF a FIXED PACKAGE or a SALE OF a RELOADABLE PACKAGE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
