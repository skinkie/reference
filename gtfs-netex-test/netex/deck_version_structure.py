from dataclasses import dataclass, field
from typing import Optional

from .deck_level_ref import DeckLevelRef
from .deck_navigation_paths_rel_structure import DeckNavigationPathsRelStructure
from .deck_path_junction_refs_rel_structure import DeckPathJunctionRefsRelStructure
from .deck_path_link_refs_rel_structure import DeckPathLinkRefsRelStructure
from .deck_spaces_rel_structure import DeckSpacesRelStructure
from .entity_in_version_structure import DataManagedObjectStructure
from .multilingual_string import MultilingualString
from .spot_columns_rel_structure import SpotColumnsRelStructure
from .spot_rows_rel_structure import SpotRowsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeckVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "Deck_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    label: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Label",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    deck_level_ref: Optional[DeckLevelRef] = field(
        default=None,
        metadata={
            "name": "DeckLevelRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    deck_spaces: Optional[DeckSpacesRelStructure] = field(
        default=None,
        metadata={
            "name": "deckSpaces",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    spot_rows: Optional[SpotRowsRelStructure] = field(
        default=None,
        metadata={
            "name": "spotRows",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    spot_columns: Optional[SpotColumnsRelStructure] = field(
        default=None,
        metadata={
            "name": "spotColumns",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    deck_path_junctions: Optional[DeckPathJunctionRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "deckPathJunctions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    deck_path_links: Optional[DeckPathLinkRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "deckPathLinks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    deck_navigation_paths: Optional[DeckNavigationPathsRelStructure] = field(
        default=None,
        metadata={
            "name": "deckNavigationPaths",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
