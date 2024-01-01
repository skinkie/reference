from dataclasses import dataclass
from .dated_special_service_ref_structure import (
    DatedSpecialServiceRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DatedSpecialServiceRef(DatedSpecialServiceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
