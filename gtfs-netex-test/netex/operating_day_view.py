from dataclasses import dataclass

from .operating_day_derived_view_structure import OperatingDayDerivedViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class OperatingDayView(OperatingDayDerivedViewStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
