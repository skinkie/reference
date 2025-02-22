from dataclasses import dataclass

from .line_version_structure import LineVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class Line(LineVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
