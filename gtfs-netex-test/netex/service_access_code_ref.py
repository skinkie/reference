from dataclasses import dataclass
from netex.service_access_code_ref_structure import ServiceAccessCodeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ServiceAccessCodeRef(ServiceAccessCodeRefStructure):
    """Reference to a SERVICE ACCESS CODE.

    +v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
