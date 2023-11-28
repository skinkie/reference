from dataclasses import dataclass, field
from netex.access_summary_versioned_child_structure import AccessSummaryVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AccessSummary(AccessSummaryVersionedChildStructure):
    """
    Summary of a feature used in NAVIGATION PATH.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
