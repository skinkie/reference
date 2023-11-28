from dataclasses import dataclass, field
from typing import List, Optional
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.distribution_assignment_ref import DistributionAssignmentRef
from netex.logical_operation_enumeration import LogicalOperationEnumeration
from netex.organisation_ref_structure import OrganisationRefStructure
from netex.point_ref_structure import PointRefStructure
from netex.validity_parameter_assignment_version_structure import ValidityParameterAssignmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SpecificParameterAssignmentVersionStructure(ValidityParameterAssignmentVersionStructure):
    """
    Type for SPECIFIC PARAMETER ASSIGNMENT.

    :ivar access_number: Access number of this specific instance.
    :ivar includes_grouping_type: Operator for Grouping Scope Elements.
        Default is OR.
    :ivar includes: Assignments Logically  included in this group.
        Groups are combined acording to the Operator.
    :ivar distribution_assignment_ref:
    :ivar retailing_organization_ref: Organizatio that sold product.
        instance.
    :ivar collection_point_ref: Point at which to collect  travel
        document.
    """
    class Meta:
        name = "SpecificParameterAssignment_VersionStructure"

    access_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "AccessNumber",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    includes_grouping_type: Optional[LogicalOperationEnumeration] = field(
        default=None,
        metadata={
            "name": "IncludesGroupingType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    includes: Optional["SpecificParameterAssignmentsRelStructure"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    distribution_assignment_ref: Optional[DistributionAssignmentRef] = field(
        default=None,
        metadata={
            "name": "DistributionAssignmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    retailing_organization_ref: Optional[OrganisationRefStructure] = field(
        default=None,
        metadata={
            "name": "RetailingOrganizationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    collection_point_ref: Optional[PointRefStructure] = field(
        default=None,
        metadata={
            "name": "CollectionPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass(unsafe_hash=True, kw_only=True)
class SpecificParameterAssignment(SpecificParameterAssignmentVersionStructure):
    """
    A VALIDITY PARAMETER ASSIGNMENT specifying practical parameters during a TRAVEL
    SPECIFICATION, within a given fare structure (e.g. the origin or destination
    zone in a zone-counting system).
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(unsafe_hash=True, kw_only=True)
class SpecificParameterAssignmentsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of SPECIFIC ACCESS RIGHT PARAMETERs.
    """
    class Meta:
        name = "specificParameterAssignments_RelStructure"

    specific_parameter_assignment: List[SpecificParameterAssignment] = field(
        default_factory=list,
        metadata={
            "name": "SpecificParameterAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
