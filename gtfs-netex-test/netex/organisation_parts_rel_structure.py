from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.control_centre import ControlCentre
from netex.control_centre_ref import ControlCentreRef
from netex.department import Department
from netex.department_ref import DepartmentRef
from netex.operating_department import OperatingDepartment
from netex.organisation_part import OrganisationPart
from netex.organisation_part_ref import OrganisationPartRef
from netex.organisational_unit import OrganisationalUnit
from netex.organisational_unit_ref import OrganisationalUnitRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class OrganisationPartsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of ORGANISATION PARTs.
    """
    class Meta:
        name = "organisationParts_RelStructure"

    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ControlCentreRef",
                    "type": ControlCentreRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OrganisationalUnitRef",
                    "type": OrganisationalUnitRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DepartmentRef",
                    "type": DepartmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OrganisationPartRef",
                    "type": OrganisationPartRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ControlCentre",
                    "type": ControlCentre,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OperatingDepartment",
                    "type": OperatingDepartment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OrganisationalUnit",
                    "type": OrganisationalUnit,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Department",
                    "type": Department,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OrganisationPart",
                    "type": OrganisationPart,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
