from dataclasses import dataclass

from .emv_card_ref_structure import EmvCardRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class EmvCardRef(EmvCardRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
