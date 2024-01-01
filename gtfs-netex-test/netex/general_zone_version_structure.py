from dataclasses import dataclass
from .zone_version_structure import ZoneVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GeneralZoneVersionStructure(ZoneVersionStructure):
    class Meta:
        name = "GeneralZone_VersionStructure"
