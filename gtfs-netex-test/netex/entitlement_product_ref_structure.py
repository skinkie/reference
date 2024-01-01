from dataclasses import dataclass
from .service_access_right_ref_structure import ServiceAccessRightRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class EntitlementProductRefStructure(ServiceAccessRightRefStructure):
    value: RestrictedVar
