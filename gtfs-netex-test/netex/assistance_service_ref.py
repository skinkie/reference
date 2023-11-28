from dataclasses import dataclass
from netex.assistance_service_ref_structure import AssistanceServiceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AssistanceServiceRef(AssistanceServiceRefStructure):
    """
    Identifier of an ASSISTANCE SERVICE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
