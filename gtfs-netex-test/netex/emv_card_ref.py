from dataclasses import dataclass
from netex.emv_card_ref_structure import EmvCardRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class EmvCardRef(EmvCardRefStructure):
    """Reference to a EMV CARD.

    +v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
