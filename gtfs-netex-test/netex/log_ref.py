from dataclasses import dataclass

from .log_ref_structure import LogRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class LogRef(LogRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
