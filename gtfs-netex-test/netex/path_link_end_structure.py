from dataclasses import dataclass, field
from typing import Optional, Union

from .deck_path_junction_ref import DeckPathJunctionRef
from .generic_path_junction_ref import GenericPathJunctionRef
from .path_junction_ref import PathJunctionRef
from .place_ref_structure import PlaceRefStructure
from .site_path_junction_ref import SitePathJunctionRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PathLinkEndStructure:
    place_ref_or_deck_path_junction_ref_or_path_junction_ref_or_site_path_junction_ref_or_generic_path_junction_ref: Optional[Union[PlaceRefStructure, DeckPathJunctionRef, PathJunctionRef, SitePathJunctionRef, GenericPathJunctionRef]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "PlaceRef",
                    "type": PlaceRefStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
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
            ),
        },
    )
