from dataclasses import dataclass
from .purpose_of_grouping_value_structure import (
    PurposeOfGroupingValueStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PurposeOfGrouping(PurposeOfGroupingValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
