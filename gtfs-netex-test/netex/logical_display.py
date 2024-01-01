from dataclasses import dataclass
from .logical_display_version_structure import LogicalDisplayVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LogicalDisplay(LogicalDisplayVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
