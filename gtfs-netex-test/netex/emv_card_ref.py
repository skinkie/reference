from dataclasses import dataclass
from .emv_card_ref_structure import EmvCardRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class EmvCardRef(EmvCardRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
