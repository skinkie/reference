from dataclasses import dataclass

from .line_ref_structure import LineRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class FlexibleLineRefStructure(LineRefStructure):
    pass
