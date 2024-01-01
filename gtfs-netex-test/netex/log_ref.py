from dataclasses import dataclass
from .log_ref_structure import LogRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LogRef(LogRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
