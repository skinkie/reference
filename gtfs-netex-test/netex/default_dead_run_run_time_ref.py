from dataclasses import dataclass
from .default_dead_run_run_time_ref_structure import (
    DefaultDeadRunRunTimeRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DefaultDeadRunRunTimeRef(DefaultDeadRunRunTimeRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
