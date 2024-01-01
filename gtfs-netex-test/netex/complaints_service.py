from dataclasses import dataclass
from .complaints_service_version_structure import (
    ComplaintsServiceVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ComplaintsService(ComplaintsServiceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
