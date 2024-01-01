from dataclasses import dataclass
from .exchanging_ref_structure import ExchangingRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ExchangingRef(ExchangingRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
