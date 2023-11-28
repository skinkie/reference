from dataclasses import dataclass, field
from typing import Optional
from netex.group_of_entities_version_structure import GroupOfEntitiesVersionStructure
from netex.transport_organisation_refs_rel_structure import TransportOrganisationRefsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GroupOfOperatorsStructure(GroupOfEntitiesVersionStructure):
    """
    Type for a GROUP OF OPERATORs.

    :ivar use_to_exclude: Whether contents of Group should be used to
        exclude (true) from a large list . The default is include
        (i.e.false)
    :ivar members: Operators in group.
    """
    use_to_exclude: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UseToExclude",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    members: Optional[TransportOrganisationRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
