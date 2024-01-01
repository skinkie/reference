from dataclasses import dataclass
from .usage_validity_period_version_structure import (
    UsageValidityPeriodVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class UsageValidityPeriod(UsageValidityPeriodVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
