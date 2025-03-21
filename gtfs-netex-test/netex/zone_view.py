from dataclasses import dataclass

from .zone_derived_view_structure import ZoneDerivedViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ZoneView(ZoneDerivedViewStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
