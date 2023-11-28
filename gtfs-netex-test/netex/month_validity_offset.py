from dataclasses import dataclass, field
from netex.month_validity_offset_versioned_structure import MonthValidityOffsetVersionedStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class MonthValidityOffset(MonthValidityOffsetVersionedStructure):
    """
    Days before (negative) or after (positive) the start of the month that a
    product with a calendar period driven activation becomes valid.

    :ivar id: Identifier of ENTITY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
