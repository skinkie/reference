from dataclasses import dataclass, field
from typing import Union

from .blacklist import Blacklist
from .blacklist_ref import BlacklistRef
from .containment_aggregation_structure import ContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class BlacklistsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "blacklists_RelStructure"

    blacklist_ref_or_blacklist: list[Union[BlacklistRef, Blacklist]] = field(
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
        },
    )
