from dataclasses import dataclass
from .service_exclusion_ref_structure import ServiceExclusionRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServiceExclusionRef(ServiceExclusionRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
