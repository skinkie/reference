from dataclasses import dataclass
from .purpose_of_grouping_ref_structure import PurposeOfGroupingRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PurposeOfGroupingRef(PurposeOfGroupingRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
