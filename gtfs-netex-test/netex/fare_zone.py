from dataclasses import dataclass
from .fare_zone_version_structure import FareZoneVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareZone(FareZoneVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
