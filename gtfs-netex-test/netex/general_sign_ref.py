from dataclasses import dataclass
from netex.general_sign_ref_structure import GeneralSignRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GeneralSignRef(GeneralSignRefStructure):
    """
    Identifier of an GENERAL SIGN.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
