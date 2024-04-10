from dataclasses import dataclass

from .property_of_day_structure import PropertyOfDayStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PropertyOfDay(PropertyOfDayStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
