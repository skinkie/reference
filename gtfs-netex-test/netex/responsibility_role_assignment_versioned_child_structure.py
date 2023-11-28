from dataclasses import dataclass, field
from typing import List, Optional
from netex.alternative_texts_rel_structure import VersionedChildStructure
from netex.data_role_type_enumeration import DataRoleTypeEnumeration
from netex.multilingual_string import MultilingualString
from netex.organisation_part_ref_structure import OrganisationPartRefStructure
from netex.organisation_ref_structure import OrganisationRefStructure
from netex.responsibility_role_ref import ResponsibilityRoleRef
from netex.responsibility_set_ref import ResponsibilitySetRef
from netex.stakeholder_role_type_enumeration import StakeholderRoleTypeEnumeration
from netex.type_of_responsibility_role_ref import TypeOfResponsibilityRoleRef
from netex.version_of_object_ref_structure import VersionOfObjectRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ResponsibilityRoleAssignmentVersionedChildStructure(VersionedChildStructure):
    """
    Type for RESPONSIBILITY ROLE ASSIGNMENT.

    :ivar responsibility_set_ref:
    :ivar description: Description of RESPONSIBILITY ROLE ASSIGNMENT.
    :ivar data_role_type: Data roles which this assignment assigns.
    :ivar stakeholder_role_type: Stakeholder roles which this assignment
        assigns.
    :ivar type_of_responsibility_role_ref_or_responsibility_role_ref:
    :ivar responsible_organisation_ref: Responsible ORGANISATION.
    :ivar responsible_part_ref: Responsible ORGANISATION PART.
    :ivar responsible_area_ref: Administrative area to which this
        RESPONSIBILITY SET is assigned.
    """
    class Meta:
        name = "ResponsibilityRoleAssignment_VersionedChildStructure"

    responsibility_set_ref: Optional[ResponsibilitySetRef] = field(
        default=None,
        metadata={
            "name": "ResponsibilitySetRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    data_role_type: List[DataRoleTypeEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "DataRoleType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    stakeholder_role_type: List[StakeholderRoleTypeEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "StakeholderRoleType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    type_of_responsibility_role_ref_or_responsibility_role_ref: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TypeOfResponsibilityRoleRef",
                    "type": TypeOfResponsibilityRoleRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ResponsibilityRoleRef",
                    "type": ResponsibilityRoleRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    responsible_organisation_ref: Optional[OrganisationRefStructure] = field(
        default=None,
        metadata={
            "name": "ResponsibleOrganisationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    responsible_part_ref: Optional[OrganisationPartRefStructure] = field(
        default=None,
        metadata={
            "name": "ResponsiblePartRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    responsible_area_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "ResponsibleAreaRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
