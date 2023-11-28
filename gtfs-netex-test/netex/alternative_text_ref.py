from dataclasses import dataclass
from netex.alternative_text_ref_structure import AlternativeTextRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AlternativeTextRef(AlternativeTextRefStructure):
    """
    Reference to an ALTERNATIVE TEXT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
