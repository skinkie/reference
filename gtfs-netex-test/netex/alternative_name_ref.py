from dataclasses import dataclass
from netex.alternative_name_ref_structure import AlternativeNameRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AlternativeNameRef(AlternativeNameRefStructure):
    """
    Reference to an ALTERNATIVE NAME.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
