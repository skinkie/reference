from dataclasses import dataclass
from .service_version_frame_structure import ServiceVersionFrameStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServiceFrame(ServiceVersionFrameStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
