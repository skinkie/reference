from dataclasses import dataclass
from .service_exclusion_version_structure import (
    ServiceExclusionVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServiceExclusion(ServiceExclusionVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
