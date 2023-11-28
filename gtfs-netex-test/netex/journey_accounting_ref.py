from dataclasses import dataclass
from netex.journey_accounting_ref_structure import JourneyAccountingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class JourneyAccountingRef(JourneyAccountingRefStructure):
    """
    Reference to a JOURNEY ACCOUNTING.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
