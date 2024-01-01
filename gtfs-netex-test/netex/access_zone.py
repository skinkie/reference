from dataclasses import dataclass
from .access_zone_version_structure import AccessZoneVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AccessZone(AccessZoneVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
