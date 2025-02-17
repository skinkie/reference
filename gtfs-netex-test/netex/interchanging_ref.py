from dataclasses import dataclass

from .interchanging_ref_structure import InterchangingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class InterchangingRef(InterchangingRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
