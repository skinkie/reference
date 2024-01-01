from dataclasses import dataclass
from .transport_administrative_zone_ref_structure import (
    TransportAdministrativeZoneRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TransportAdministrativeZoneRef(TransportAdministrativeZoneRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
