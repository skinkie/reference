from dataclasses import dataclass

from .suspending_version_structure import SuspendingVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class Suspending(SuspendingVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
