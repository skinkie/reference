from dataclasses import dataclass

from .usage_validity_period_version_structure import UsageValidityPeriodVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class UsageValidityPeriod(UsageValidityPeriodVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
