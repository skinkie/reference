from dataclasses import dataclass

from .time_structure_factor_ref_structure import TimeStructureFactorRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TimeStructureFactorRef(TimeStructureFactorRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
