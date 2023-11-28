from dataclasses import dataclass
from netex.property_of_day_structure import PropertyOfDayStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PropertyOfDay(PropertyOfDayStructure):
    """
    A property which a day may possess, such as school holiday, weekday, summer,
    winter etc.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
