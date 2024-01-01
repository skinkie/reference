from dataclasses import dataclass
from .general_zone_version_structure import GeneralZoneVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GeneralZone(GeneralZoneVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
