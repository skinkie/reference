from dataclasses import dataclass

from .zone_projection_ref_structure import ZoneProjectionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TopographicProjectionRefStructure(ZoneProjectionRefStructure):
    pass
