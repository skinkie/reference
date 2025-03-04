from dataclasses import dataclass

from .cancelling_version_structure import CancellingVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class Cancelling(CancellingVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
