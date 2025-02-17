from dataclasses import dataclass

from .zone_version_structure import ZoneVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class Zone(ZoneVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
