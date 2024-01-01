from dataclasses import dataclass
from .fare_contract_version_structure import FareContractVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareContract(FareContractVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
