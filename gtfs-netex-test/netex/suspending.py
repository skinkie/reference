from dataclasses import dataclass, field
from netex.suspending_version_structure import SuspendingVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class Suspending(SuspendingVersionStructure):
    """
    Conditions governing suspension of a FARE PRODUCT, e.g.  period pass or
    subscription.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
