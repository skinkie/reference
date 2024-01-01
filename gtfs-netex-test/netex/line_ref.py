from dataclasses import dataclass
from .line_ref_structure import LineRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LineRef(LineRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
