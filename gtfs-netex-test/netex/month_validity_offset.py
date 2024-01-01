from dataclasses import dataclass
from .month_validity_offset_versioned_structure import (
    MonthValidityOffsetVersionedStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class MonthValidityOffset(MonthValidityOffsetVersionedStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
