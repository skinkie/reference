from dataclasses import dataclass

from .operational_context_version_structure import OperationalContextVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class OperationalContext(OperationalContextVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
