from dataclasses import dataclass, field
from typing import List, Union

from .deck_navigation_path_ref import DeckNavigationPathRef
from .generic_navigation_path_ref import GenericNavigationPathRef
from .navigation_path_ref import NavigationPathRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .site_navigation_path_ref import SiteNavigationPathRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GenericNavigationPathRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "GenericNavigationPathRefs_RelStructure"

    generic_navigation_path_ref: List[Union[DeckNavigationPathRef, NavigationPathRef, SiteNavigationPathRef, GenericNavigationPathRef]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DeckNavigationPathRef",
                    "type": DeckNavigationPathRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "NavigationPathRef",
                    "type": NavigationPathRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SiteNavigationPathRef",
                    "type": SiteNavigationPathRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GenericNavigationPathRef",
                    "type": GenericNavigationPathRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
