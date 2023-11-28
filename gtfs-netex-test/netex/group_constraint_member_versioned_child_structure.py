from dataclasses import dataclass, field
from typing import Optional
from netex.alternative_texts_rel_structure import VersionedChildStructure
from netex.class_ref_structure import ClassRefStructure
from netex.purpose_of_grouping_ref_structure import PurposeOfGroupingRefStructure
from netex.type_of_value_ref_structure import TypeOfValueRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GroupConstraintMemberVersionedChildStructure(VersionedChildStructure):
    """Type for a Group of Entities Constraint Member.

    Specifies an allowed class to include in a group.

    :ivar purpose_of_grouping_ref: Reference to a PUPOSE OF GROUPING  to
        which this member belongs.  If given by context does not need to
        be specified.
    :ivar member_class_ref: Allowed Class of Entity.
    :ivar member_type_of_value_ref: Allowed type of Entity.
    """
    class Meta:
        name = "GroupConstraintMember_VersionedChildStructure"

    purpose_of_grouping_ref: Optional[PurposeOfGroupingRefStructure] = field(
        default=None,
        metadata={
            "name": "PurposeOfGroupingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    member_class_ref: ClassRefStructure = field(
        metadata={
            "name": "MemberClassRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    member_type_of_value_ref: Optional[TypeOfValueRefStructure] = field(
        default=None,
        metadata={
            "name": "MemberTypeOfValueRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
