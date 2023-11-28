from dataclasses import dataclass
from netex.zone_derived_view_structure import ZoneDerivedViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ZoneView(ZoneDerivedViewStructure):
    """Simplified view of SCHEDULED STOP POINT.

    Includes derived some propertries of a stop.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
