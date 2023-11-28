from dataclasses import dataclass, field
from typing import List
from netex.blacklist import Blacklist
from netex.blacklist_ref import BlacklistRef
from netex.containment_aggregation_structure import ContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class BlacklistsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of BLACKLISTs.
    """
    class Meta:
        name = "blacklists_RelStructure"

    blacklist_ref_or_blacklist: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "BlacklistRef",
                    "type": BlacklistRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Blacklist",
                    "type": Blacklist,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
