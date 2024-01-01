from dataclasses import dataclass
from .service_link_in_sequence_ref_structure import (
    ServiceLinkInSequenceRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServiceLinkInSequenceRef(ServiceLinkInSequenceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
