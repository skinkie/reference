from dataclasses import dataclass
from .money_service_version_structure import MoneyServiceVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class MoneyService(MoneyServiceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
