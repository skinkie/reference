from dataclasses import dataclass

from .cancelling_ref_structure import CancellingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CancellingRef(CancellingRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
