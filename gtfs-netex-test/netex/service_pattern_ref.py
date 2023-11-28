from dataclasses import dataclass
from netex.service_pattern_ref_structure import ServicePatternRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ServicePatternRef(ServicePatternRefStructure):
    """
    Reference to a SERVICE PATTERN.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
