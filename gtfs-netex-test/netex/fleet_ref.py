from dataclasses import dataclass
from .fleet_ref_structure import FleetRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FleetRef(FleetRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
