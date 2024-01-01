from dataclasses import dataclass
from .type_of_time_demand_type_ref_structure import (
    TypeOfTimeDemandTypeRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfTimeDemandTypeRef(TypeOfTimeDemandTypeRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
