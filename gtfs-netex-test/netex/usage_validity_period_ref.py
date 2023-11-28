from dataclasses import dataclass
from netex.usage_validity_period_ref_structure import UsageValidityPeriodRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class UsageValidityPeriodRef(UsageValidityPeriodRefStructure):
    """
    Reference to a USAGE VALIDITY PERIOD.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
