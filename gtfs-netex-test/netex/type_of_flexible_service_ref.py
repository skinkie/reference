from dataclasses import dataclass
from .type_of_flexible_service_ref_structure import (
    TypeOfFlexibleServiceRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfFlexibleServiceRef(TypeOfFlexibleServiceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
