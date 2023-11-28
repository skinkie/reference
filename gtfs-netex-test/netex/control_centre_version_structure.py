from dataclasses import dataclass, field
from typing import Optional
from netex.department_ref import DepartmentRef
from netex.multilingual_string import MultilingualString
from netex.organisation_part_version_structure import OrganisationPartVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ControlCentreVersionStructure(OrganisationPartVersionStructure):
    """
    Type for CONTROL CENTRE.

    :ivar number: Number used to identify CONTROL CENTRE.
    :ivar control_centre_code: Unique alphanumeric identification of
        CONTROL CENTRE  used to identify source  of request to external
        systems.
    :ivar department_ref:
    """
    class Meta:
        name = "ControlCentre_VersionStructure"

    number: Optional[int] = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    control_centre_code: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "ControlCentreCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    department_ref: Optional[DepartmentRef] = field(
        default=None,
        metadata={
            "name": "DepartmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
