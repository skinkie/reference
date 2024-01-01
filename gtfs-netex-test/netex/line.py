from dataclasses import dataclass
from .line_version_structure import LineVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Line(LineVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
