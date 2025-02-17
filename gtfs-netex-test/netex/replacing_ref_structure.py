from dataclasses import dataclass

from .reselling_ref_structure import ResellingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ReplacingRefStructure(ResellingRefStructure):
    pass
