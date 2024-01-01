from dataclasses import dataclass
from .point_ref_structure import PointRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RoutePointRefStructure(PointRefStructure):
    value: RestrictedVar
