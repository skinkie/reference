from dataclasses import dataclass
from netex.dated_special_service_ref_structure import DatedSpecialServiceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DatedSpecialServiceRef(DatedSpecialServiceRefStructure):
    """
    Reference to a DATED SPECIAL SERVICE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
