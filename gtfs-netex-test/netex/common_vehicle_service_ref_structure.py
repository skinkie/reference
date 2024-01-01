from dataclasses import dataclass
from .mobility_service_ref_structure import MobilityServiceRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CommonVehicleServiceRefStructure(MobilityServiceRefStructure):
    value: RestrictedVar
