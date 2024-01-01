from dataclasses import dataclass
from .relief_point_version_structure import ReliefPointVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ReliefPoint(ReliefPointVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
