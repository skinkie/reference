from dataclasses import dataclass
from .point_on_link_ref_structure_2 import PointOnLinkRefStructure2


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PointOnLinkRefStructure1(PointOnLinkRefStructure2):
    class Meta:
        name = "PointOnLinkRefStructure"

    value: RestrictedVar
