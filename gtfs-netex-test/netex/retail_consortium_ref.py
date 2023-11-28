from dataclasses import dataclass
from netex.retail_consortium_ref_structure import RetailConsortiumRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RetailConsortiumRef(RetailConsortiumRefStructure):
    """
    Reference to a RETAIL CONSORTIUM.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
