from dataclasses import dataclass
from .taxi_service_ref_structure import TaxiServiceRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TaxiServiceRef(TaxiServiceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
