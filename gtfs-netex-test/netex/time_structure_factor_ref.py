from dataclasses import dataclass
from .time_structure_factor_ref_structure import (
    TimeStructureFactorRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TimeStructureFactorRef(TimeStructureFactorRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
