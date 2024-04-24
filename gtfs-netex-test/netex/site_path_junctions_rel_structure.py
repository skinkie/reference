from dataclasses import dataclass, field
from typing import List, Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .deck_path_junction_ref import DeckPathJunctionRef
from .generic_path_junction_ref import GenericPathJunctionRef
from .path_junction import PathJunction
from .path_junction_ref import PathJunctionRef
from .site_path_junction import SitePathJunction
from .site_path_junction_ref import SitePathJunctionRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SitePathJunctionsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "sitePathJunctions_RelStructure"

    deck_path_junction_ref_or_path_junction_ref_or_site_path_junction_ref_or_generic_path_junction_ref_or_site_path_junction_or_path_junction: List[Union[DeckPathJunctionRef, PathJunctionRef, SitePathJunctionRef, GenericPathJunctionRef, SitePathJunction, PathJunction]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DeckPathJunctionRef",
                    "type": DeckPathJunctionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PathJunctionRef",
                    "type": PathJunctionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SitePathJunctionRef",
                    "type": SitePathJunctionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GenericPathJunctionRef",
                    "type": GenericPathJunctionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SitePathJunction",
                    "type": SitePathJunction,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PathJunction",
                    "type": PathJunction,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
