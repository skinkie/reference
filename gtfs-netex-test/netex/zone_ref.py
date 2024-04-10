from dataclasses import dataclass

from .zone_ref_structure import ZoneRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ZoneRef(ZoneRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
