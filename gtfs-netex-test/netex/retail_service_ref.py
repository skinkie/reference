from dataclasses import dataclass
from netex.retail_service_ref_structure import RetailServiceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RetailServiceRef(RetailServiceRefStructure):
    """
    Identifier of an RETAIL SERVICE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
