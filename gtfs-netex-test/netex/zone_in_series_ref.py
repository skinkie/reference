from dataclasses import dataclass

from .zone_in_series_ref_structure import ZoneInSeriesRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ZoneInSeriesRef(ZoneInSeriesRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
