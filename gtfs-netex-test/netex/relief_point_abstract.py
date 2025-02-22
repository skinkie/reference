from dataclasses import dataclass

from .timing_point_version_structure import TimingPointVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ReliefPointAbstract(TimingPointVersionStructure):
    class Meta:
        name = "ReliefPoint_"
        namespace = "http://www.netex.org.uk/netex"
