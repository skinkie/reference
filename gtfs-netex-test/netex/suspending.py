from dataclasses import dataclass
from .suspending_version_structure import SuspendingVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Suspending(SuspendingVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
