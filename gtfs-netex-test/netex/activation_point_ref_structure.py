from dataclasses import dataclass

from .point_ref_structure import PointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ActivationPointRefStructure(PointRefStructure):
    pass
