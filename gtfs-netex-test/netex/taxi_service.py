from dataclasses import dataclass
from .taxi_service_version_structure import TaxiServiceVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TaxiService(TaxiServiceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
