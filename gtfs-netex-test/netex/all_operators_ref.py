from dataclasses import dataclass
from .all_operators_ref_structure import AllOperatorsRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AllOperatorsRef(AllOperatorsRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
