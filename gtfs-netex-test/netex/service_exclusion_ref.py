from dataclasses import dataclass
from netex.service_exclusion_ref_structure import ServiceExclusionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ServiceExclusionRef(ServiceExclusionRefStructure):
    """
    Reference to a SERVICE EXCLUSION.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
