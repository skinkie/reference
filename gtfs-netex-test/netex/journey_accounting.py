from dataclasses import dataclass
from .journey_accounting_version_structure import (
    JourneyAccountingVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class JourneyAccounting(JourneyAccountingVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
