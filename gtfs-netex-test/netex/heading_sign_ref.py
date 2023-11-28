from dataclasses import dataclass
from netex.heading_sign_ref_structure import HeadingSignRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class HeadingSignRef(HeadingSignRefStructure):
    """
    Identifier of an HEADING SIGN.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
