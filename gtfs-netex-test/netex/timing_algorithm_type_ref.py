from dataclasses import dataclass
from .timing_algorithm_type_ref_structure import (
    TimingAlgorithmTypeRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TimingAlgorithmTypeRef(TimingAlgorithmTypeRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
