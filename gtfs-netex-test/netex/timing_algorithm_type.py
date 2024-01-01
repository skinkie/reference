from dataclasses import dataclass
from .timing_algorithm_type_value_structure import (
    TimingAlgorithmTypeValueStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TimingAlgorithmType(TimingAlgorithmTypeValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
