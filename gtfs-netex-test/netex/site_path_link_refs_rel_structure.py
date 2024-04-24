from dataclasses import dataclass, field
from typing import List, Union

from .deck_path_link_ref import DeckPathLinkRef
from .generic_path_link_ref import GenericPathLinkRef
from .off_site_path_link_ref import OffSitePathLinkRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .path_link_ref import PathLinkRef
from .path_link_ref_by_value import PathLinkRefByValue
from .site_path_link_ref import SitePathLinkRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SitePathLinkRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "sitePathLinkRefs_RelStructure"

    deck_path_link_ref_or_off_site_path_link_ref_or_path_link_ref_or_site_path_link_ref_or_generic_path_link_ref_or_path_link_ref_by_value: List[Union[DeckPathLinkRef, OffSitePathLinkRef, PathLinkRef, SitePathLinkRef, GenericPathLinkRef, PathLinkRefByValue]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DeckPathLinkRef",
                    "type": DeckPathLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OffSitePathLinkRef",
                    "type": OffSitePathLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PathLinkRef",
                    "type": PathLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SitePathLinkRef",
                    "type": SitePathLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GenericPathLinkRef",
                    "type": GenericPathLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PathLinkRefByValue",
                    "type": PathLinkRefByValue,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
