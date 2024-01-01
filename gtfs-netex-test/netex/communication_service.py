from dataclasses import dataclass
from .communication_service_version_structure import (
    CommunicationServiceVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CommunicationService(CommunicationServiceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
