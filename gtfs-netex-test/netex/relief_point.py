from dataclasses import dataclass

from .relief_point_version_structure import ReliefPointVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ReliefPoint(ReliefPointVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
