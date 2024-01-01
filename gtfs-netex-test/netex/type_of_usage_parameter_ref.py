from dataclasses import dataclass
from .type_of_usage_parameter_ref_structure import (
    TypeOfUsageParameterRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfUsageParameterRef(TypeOfUsageParameterRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
