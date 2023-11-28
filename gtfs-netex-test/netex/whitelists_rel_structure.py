from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.whitelist import Whitelist
from netex.whitelist_ref import WhitelistRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class WhitelistsRelStructure(ContainmentAggregationStructure):
    """Type for a list of WHITELISTs.

    +v1.1
    """
    class Meta:
        name = "whitelists_RelStructure"

    whitelist_ref_or_whitelist: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "WhitelistRef",
                    "type": WhitelistRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Whitelist",
                    "type": Whitelist,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
