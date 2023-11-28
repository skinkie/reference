from dataclasses import dataclass, field
from typing import Optional
from netex.display_assignment_version_structure import DisplayAssignmentVersionStructure
from netex.status_enumeration import StatusEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DisplayAssignment(DisplayAssignmentVersionStructure):
    """
    The assignment of one STOP POINT and one JOURNEY PATTERN to a PASSENGER
    INFORMATION EQUIPMENT, specifying that information on this STOP POINT and this
    JOURNEY PATTERN will be provided (e.g. displayed, printed).

    :ivar name_of_class: Name of Class of the ENTITY. Allows reflection.
        Fixed for each ENTITY type.
    :ivar data_source_ref: Name of source of the data.
    :ivar status: Whether ENTITY is currently in use. Default is
        "released"
    :ivar derived_from_version_ref: Version of this object from which
        this version of ENTITY was derived.
    :ivar id: Identifier of DISPLAY ASSIGNMENT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    name_of_class: Optional[str] = field(
        default=None,
        metadata={
            "name": "nameOfClass",
            "type": "Attribute",
        }
    )
    data_source_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "dataSourceRef",
            "type": "Attribute",
        }
    )
    status: StatusEnumeration = field(
        default=StatusEnumeration.ACTIVE,
        metadata={
            "type": "Attribute",
        }
    )
    derived_from_version_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "derivedFromVersionRef",
            "type": "Attribute",
        }
    )
    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
