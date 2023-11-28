from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.version import Version
from netex.version_ref import VersionRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VersionsRelStructure(ContainmentAggregationStructure):
    """
    Type for containment of a VERSION.
    """
    class Meta:
        name = "versions_RelStructure"

    version_ref_or_version: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "VersionRef",
                    "type": VersionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Version",
                    "type": Version,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
