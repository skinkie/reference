from dataclasses import dataclass
from .administrative_zone_ref_structure import AdministrativeZoneRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TransportAdministrativeZoneRefStructure(AdministrativeZoneRefStructure):
    pass
