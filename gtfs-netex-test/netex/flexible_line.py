from dataclasses import dataclass

from .flexible_line_version_structure import FlexibleLineVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class FlexibleLine(FlexibleLineVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
