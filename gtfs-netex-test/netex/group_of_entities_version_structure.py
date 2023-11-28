from dataclasses import dataclass, field
from typing import List, Optional
from netex.alternative_texts_rel_structure import DataManagedObjectStructure
from netex.info_links_rel_structure import InfoLinksRelStructure
from netex.multilingual_string import MultilingualString
from netex.private_code import PrivateCode
from netex.purpose_of_grouping_ref import PurposeOfGroupingRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GroupOfEntitiesVersionStructure(DataManagedObjectStructure):
    """
    Type for a GROUP OF ENTITies.

    :ivar name: Name of GROUP OF ENTITies.
    :ivar short_name: Short Name of GROUP OF ENTITies.
    :ivar description: Further Description of a GROUP OF ENTITies.
    :ivar purpose_of_grouping_ref: Reference to a PURPOSE OF GROUPING.
    :ivar private_code:
    :ivar info_links: Hyperlinks associated with GROUP OF ENTITIES.
    """
    class Meta:
        name = "GroupOfEntities_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    short_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    description: List[MultilingualString] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    purpose_of_grouping_ref: Optional[PurposeOfGroupingRef] = field(
        default=None,
        metadata={
            "name": "PurposeOfGroupingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    private_code: Optional[PrivateCode] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    info_links: Optional[InfoLinksRelStructure] = field(
        default=None,
        metadata={
            "name": "infoLinks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
