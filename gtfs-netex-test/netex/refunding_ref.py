from dataclasses import dataclass
from .refunding_ref_structure import RefundingRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RefundingRef(RefundingRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
