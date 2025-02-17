from dataclasses import dataclass

from .service_access_right_ref_structure import ServiceAccessRightRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class EntitlementProductRefStructure(ServiceAccessRightRefStructure):
    pass
