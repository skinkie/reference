from dataclasses import dataclass
from netex.smartcard_ref_structure import SmartcardRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SmartcardRef(SmartcardRefStructure):
    """Reference to a SMARTCARD.

    +v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
